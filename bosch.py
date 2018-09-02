# BME280 code from https://github.com/catdog2/mpy_bme280_esp8266
# todo:  take 16 samples and use median?

import array
from machine import I2C, Pin   # create an I2C bus object for BME280 sensor
import bme280

i2c = I2C(scl=Pin(5), sda=Pin(4))
bme = bme280.BME280(i2c=i2c)

def median(lst):
    quotient, remainder = divmod(len(lst), 2)
    if remainder:
        return sorted(lst)[quotient]
    return sum(sorted(lst)[quotient - 1:quotient + 1]) / 2.

def measure(tph):
	print("BME Values:", bme.values)
	raw = bme.read_compensated_data()
	tph[0] = (raw[0]/100.)*(9/5)+32  # Fahrenheit  
	tph[1] = raw[1]/(256*1000.)      # kPa
	tph[2] = raw[2]/1024.            # % 
	return(tph)
