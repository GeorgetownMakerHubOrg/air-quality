# The MIT License (MIT) - https://opensource.org/licenses/MIT
# STIA436 Course - Spring 2019
# Professor Colin McCormick & Father Chris Wagner
# F. Pascal Girard
#
# With the exception of implementing a ring buffer to eliminate memory over-allocation, 
# full credit for this code goes to: https://github.com/pimoroni/bme680-python (see examples/read-all.py)
# 
# also look at: https://github.com/BoschSensortec/BME680_driver for configuration information
# this driver is too large for ESP8266's memory.
#
import bme680
import time

from machine import I2C, Pin
from usmbus import SMBus
from bme680 import constants

i2c = SMBus(scl=Pin(22), sda=Pin(21))    # ESP32 only
sensor = bme680.BME680(i2c_device=i2c, i2c_addr=constants.I2C_ADDR_SECONDARY)

# These oversampling settings can be tweaked to 
# change the balance between accuracy and noise in
# the data.

sensor.set_humidity_oversample(constants.OS_2X)
sensor.set_pressure_oversample(constants.OS_4X)
sensor.set_temperature_oversample(constants.OS_8X)
sensor.set_filter(constants.FILTER_SIZE_3)
sensor.set_gas_status(constants.ENABLE_GAS_MEAS)

# Up to 10 heater profiles can be configured, each
# with their own temperature and duration.
# sensor.set_gas_heater_profile(200, 150, nb_profile=1)
# sensor.select_gas_heater_profile(1)
sensor.set_gas_heater_temperature(320)
sensor.set_gas_heater_duration(150)
sensor.select_gas_heater_profile(0)

RING_BUFFER_SIZE = 10

def measure():
    try:
    # Collect gas resistance burn-in values, then use the average
    # of the last 50 values to set the upper limit for calculating
    # gas_baseline.
        gas_buffer = []
        i = 0
        while not sensor.data.heat_stable:
            sensor.get_sensor_data()
            gas = sensor.data.gas_resistance
            if len(gas_buffer) >= RING_BUFFER_SIZE:
                gas_buffer.pop(0)
            gas_buffer.append(gas)
            print("Gas: {0} Ohms".format(gas), "Iteration:", i)
            i += 1
            time.sleep(1)

        gas_baseline = sum(gas_buffer) / len(gas_buffer)

        if sensor.get_sensor_data():
            # output = "{0:.2f} C,{1:.2f} hPa,{2:.2f} %RH".format(sensor.data.temperature, sensor.data.pressure, sensor.data.humidity)
            data = { 
            "temperature": sensor.data.temperature,           # Fahrenheit  
            "pressure": sensor.data.pressure,                 # kPa
            "humidity": sensor.data.humidity                  # % 
            }
            if sensor.data.heat_stable:
                data["voc"] = sensor.data.gas_resistance
        return(data)

    except KeyboardInterrupt:
        pass
