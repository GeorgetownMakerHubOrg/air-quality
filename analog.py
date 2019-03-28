# The MIT License (MIT) - https://opensource.org/licenses/MIT
# STIA436 Course - Spring 2019
# Professor Colin McCormick & Father Chris Wagner
# F. Pascal Girard
#
# ADS1x15 code from https://github.com/adafruit/micropython-adafruit-ads1015
# Keep in mind that this I2C board can have up to 4 addresses using the address pin.
# Default is 0x48.
#

import array
from machine import I2C, Pin   			  # create an I2C bus object for all I2C-based sensors.
import ads1x15

i2c = I2C(scl=Pin(5), sda=Pin(4))		  # create the I2C bus
# 16 bit 
raw = ads1x15.ADS1115(i2c, address=0x48)

def measure():
	return {
        "A0": raw.read(0),    
        "A1": raw.read(1),
        "A2": raw.read(2),
        "A3": raw.read(3)
    }