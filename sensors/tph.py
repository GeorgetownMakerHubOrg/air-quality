# GNU General Public License <https://www.gnu.org/licenses>
# STIA436 Course - Spring 2019
# Professor Colin McCormick & Father Chris Wagner
# Copyright (c) 2019 F. Pascal Girard, Colton Padden
#
# BME280 code from https://github.com/catdog2/mpy_bme280_esp8266
# Given that we might have multiple Bosch sensors on I2C bus, we might have to alter the
# BME280 default address when we instance it - BME280_I2CADDR = 0x76
#
# Do we want to use median() to take multiple samples to remove noise?
# it would easy to take 8 samples and grab the median

from machine import I2C, Pin

from config import DEBUG
from sensors.bme280 import bme280


class tph(object):
    """
    Convenience wrapper for measurements with the bme280 sensor

    Example Usage:
    >> tph_1 = tph(5, 4)   # i2c bus for ESP8266
    >> tph_2 = tph(22, 21) # i2c bus for Lolin ESP32
    >> tph_2.measure()
    """

    def __init__(self, scl_pin, sda_pin, address=0x76):
        i2c = I2C(scl=Pin(scl_pin), sda=Pin(sda_pin))
        self.address = address
        self.bme280 = bme280.BME280(i2c=i2c, address=address)

    def median(self, lst):
        quotient, remainder = divmod(len(lst), 2)
        if remainder:
            return sorted(lst)[quotient]
        return sum(sorted(lst)[quotient - 1: quotient + 1]) / 2.0

    def measure(self):

        if DEBUG:
            print("BME 280 Values:", self.bme280.values)

        raw = self.bme280.read_compensated_data()
        return {
            "temperature_" + str(self.address): (raw[0] / 100.0) * (9 / 5) + 32,  # Fahrenheit
            "pressure_" + str(self.address): raw[1] / (256 * 1000.0),             # kPa
            "humidity_" + str(self.address): raw[2] / 1024.0,                     # %
        }
