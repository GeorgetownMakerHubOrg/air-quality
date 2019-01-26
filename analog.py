#
#
# ADS1x15 code from 
# Keep in mind that this I2C board can have up to 4 addresses using the address pin.
# Default is 0x48.
#

import array
from machine import I2C, Pin   			  # create an I2C bus object for all I2C-based sensors.
import ads1x15

i2c = I2C(scl=Pin(5), sda=Pin(4))		  # create the I2C bus
raw = ads1x15.ADS1115(i2c, address=0x48)

def measure(adc):
	adc[0] = raw.read(0)             # Channel 0  
	adc[1] = raw.read(1)             # Channel 1
	adc[2] = raw.read(2)             # Channel 2
	adc[3] = raw.read(3)             # Channel 3
	print("Analog values: ", adc)
	return(adc)
