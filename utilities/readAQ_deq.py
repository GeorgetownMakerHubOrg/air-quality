#!/usr/bin/env python

import time
import bme680

from machine import I2C, Pin
from usmbus import SMBus
from bme680 import constants

i2c_bus = SMBus(scl=Pin(22), sda=Pin(21))
address = i2c_bus.scan()[0]                           # expect 0x77 or 119 decimal
register = 0xd0
chipid = i2c_bus.read_byte_data(address, register)    # expect 0x61 or 97 decimal
print("Address/Chip Id is:", address,"/",chipid)
sensor = bme680.BME680(i2c_device=i2c_bus, i2c_addr=constants.I2C_ADDR_SECONDARY)

print("""Estimate indoor air quality

Runs the sensor for a burn-in period, then uses a 
combination of relative humidity and gas resistance
to estimate indoor air quality as a percentage.

Press Ctrl+C to exit

""")
sensor.set_humidity_oversample(constants.OS_2X)
sensor.set_pressure_oversample(constants.OS_4X)
sensor.set_temperature_oversample(constants.OS_8X)
sensor.set_filter(constants.FILTER_SIZE_3)
sensor.set_gas_status(constants.ENABLE_GAS_MEAS)

sensor.set_gas_heater_temperature(320)
sensor.set_gas_heater_duration(150)
sensor.select_gas_heater_profile(0)

# start_time and curr_time ensure that the 
# burn_in_time (in seconds) is kept track of.

start_time = time.time()
curr_time = time.time()
burn_in_time = 300
RING_BUFFER_SIZE = 50


try:
    # Collect gas resistance burn-in values, then use the average
    # of the last 50 values to set the upper limit for calculating
    # gas_baseline.
    print("Collecting gas resistance burn-in data for 5 mins\n")
    gas_buffer = []
    i = 0
    
    while curr_time - start_time < burn_in_time:
        curr_time = time.time()
        i += 1
        if sensor.get_sensor_data() and sensor.data.heat_stable:
            gas = sensor.data.gas_resistance
            if len(gas_buffer) >= RING_BUFFER_SIZE:
                gas_buffer.pop(0)
            gas_buffer.append(gas)
            print("Gas: {0} Ohms".format(gas), "Iteration:", i)
            time.sleep(1)

    gas_baseline = sum(gas_buffer) / RING_BUFFER_SIZE

    # Set the humidity baseline to 40%, an optimal indoor humidity.
    hum_baseline = 40.0

    # This sets the balance between humidity and gas reading in the 
    # calculation of air_quality_score (25:75, humidity:gas)
    hum_weighting = 0.25

    print("Gas baseline: {0} Ohms, humidity baseline: {1:.2f} %RH\n".format(gas_baseline, hum_baseline))

    while True:
        if sensor.get_sensor_data() and sensor.data.heat_stable:
            gas = sensor.data.gas_resistance
            gas_offset = gas_baseline - gas

            hum = sensor.data.humidity
            hum_offset = hum - hum_baseline

            # Calculate hum_score as the distance from the hum_baseline.
            if hum_offset > 0:
                hum_score = (100 - hum_baseline - hum_offset) / (100 - hum_baseline) * (hum_weighting * 100)

            else:
                hum_score = (hum_baseline + hum_offset) / hum_baseline * (hum_weighting * 100)

            # Calculate gas_score as the distance from the gas_baseline.
            if gas_offset > 0:
                gas_score = (gas / gas_baseline) * (100 - (hum_weighting * 100))

            else:
                gas_score = 100 - (hum_weighting * 100)

            # Calculate air_quality_score. 
            air_quality_score = hum_score + gas_score

            print("Gas: {0:.2f} Ohms,humidity: {1:.2f} %RH,air quality: {2:.2f}".format(gas, hum, air_quality_score))
            time.sleep(1)

except KeyboardInterrupt:
    pass
