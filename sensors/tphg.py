# GNU General Public License <https://www.gnu.org/licenses>
# STIA436 Course - Spring 2019
# Professor Colin McCormick & Father Chris Wagner
# Copyright (c) 2019 F. Pascal Girard
#
# With the exception of implementing a ring buffer to eliminate memory over-allocation,
# full credit for this code goes to: https://github.com/pimoroni/bme680-python (see examples/read-all.py)
#
# also look at: https://github.com/BoschSensortec/BME680_driver for configuration information
# this driver is too large for ESP8266's memory.

import time

from machine import Pin

from config import DEBUG
from lib import bme680
from lib.bme680 import constants
from lib.usmbus import SMBus


RING_BUFFER_SIZE = 10


class tphg(object):
    """
    Convenience wrapper for measurements with the bme680 sensor

    Example Usage:
    >> tphg_1 = tphg(22, 21)
    >> tphg_1.measure()
    """

    def __init__(self, scl_pin, sda_pin, address=constants.I2C_ADDR_SECONDARY):

        i2c = SMBus(scl=Pin(scl_pin), sda=Pin(sda_pin))  # ESP32 only

        self.address = address
        self.sensor = bme680.BME680(i2c_device=i2c, i2c_addr=address)

        # These oversampling settings can be tweaked to
        # change the balance between accuracy and noise in
        # the data.
        self.sensor.set_humidity_oversample(constants.OS_2X)
        self.sensor.set_pressure_oversample(constants.OS_4X)
        self.sensor.set_temperature_oversample(constants.OS_8X)
        self.sensor.set_filter(constants.FILTER_SIZE_3)
        self.sensor.set_gas_status(constants.ENABLE_GAS_MEAS)

        # Up to 10 heater profiles can be configured, each
        # with their own temperature and duration.
        # sensor.set_gas_heater_profile(200, 150, nb_profile=1)
        # sensor.select_gas_heater_profile(1)
        self.sensor.set_gas_heater_temperature(320)
        self.sensor.set_gas_heater_duration(150)
        self.sensor.select_gas_heater_profile(0)

    def measure(self):
        try:
            # Collect gas resistance burn-in values, then use the average
            # of the last 50 values to set the upper limit for calculating
            # gas_baseline.
            gas_buffer = []
            i = 0
            while not self.sensor.data.heat_stable:
                self.sensor.get_sensor_data()
                gas = self.sensor.data.gas_resistance
                if len(gas_buffer) >= RING_BUFFER_SIZE:
                    gas_buffer.pop(0)
                gas_buffer.append(gas)

                if DEBUG:
                    print("Gas: {0} Ohms".format(gas), "Iteration:", i)

                i += 1
                time.sleep(1)

            # NOTE: this variable is unused
            # gas_baseline = sum(gas_buffer) / len(gas_buffer)

            if self.sensor.get_sensor_data():
                measurements = {
                    "temperature-bme680_0x{:02x}".format(self.address): self.sensor.data.temperature,  # Celcius
                    "pressure-bme680_0x{:02x}".format(self.address): self.sensor.data.pressure/10.,    # kPa
                    "humidity-bme680_0x{:02x}".format(self.address): self.sensor.data.humidity,        # %
                }
                if self.sensor.data.heat_stable:
                    measurements["voc"] = self.sensor.data.gas_resistance

                if DEBUG:
                    print(measurements)

            return measurements

        except KeyboardInterrupt:
            pass
