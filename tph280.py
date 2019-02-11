#
# BME280 code from https://github.com/catdog2/mpy_bme280_esp8266
# Given that we might have multiple Bosch sensors on I2C bus, we might have to alter the
# BME280 default address when we instance it - BME280_I2CADDR = 0x76 
# 
# Do we want to use median() to take multiple samples to remove noise?

import array
from machine import I2C, Pin   # create an I2C bus object for all I2C-based sensors.
import bme280

i2c = I2C(scl=Pin(5), sda=Pin(4))		  # create the I2C bus
bme280 = bme280.BME280(i2c=i2c, address=0x76)

# it would easy to take 8 samples and grab the median

def median(lst):
    quotient, remainder = divmod(len(lst), 2)
    if remainder:
        return sorted(lst)[quotient]
    return sum(sorted(lst)[quotient - 1:quotient + 1]) / 2.

def measure():
	print("BME 280 Values:", bme280.values)
	raw = bme280.read_compensated_data()
	return { 
        "temperature": (raw[0]/100.)*(9/5)+32,     # Fahrenheit  
        "pressure": raw[1]/(256*1000.0),           # kPa
        "humidity": raw[2]/1024.0                  # % 
    }