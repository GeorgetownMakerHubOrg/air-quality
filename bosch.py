# BME280 code from https://github.com/catdog2/mpy_bme280_esp8266

import array
from machine import I2C, Pin   # create an I2C bus object for BME280 sensor
import bme280

i2c = I2C(scl=Pin(5), sda=Pin(4))
bme = bme280.BME280(i2c=i2c)

def measure(tph):
	print("BME Values:", bme.values)
	return(bme.read_compensated_data())
