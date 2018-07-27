# BME280 code from https://github.com/catdog2/mpy_bme280_esp8266

import array
from machine import I2C, Pin   # create an I2C bus object for BME280 sensor
import wifi, bme280

i2c = I2C(scl=Pin(5), sda=Pin(4))
bme = bme280.BME280(i2c=i2c)

def to_F(value):
	return(value*(9/5)+32)

def measure():
	print("BME Values:", bme.values)
	data = bme.read_compensated_data()
	wifi.post("temperature",to_F(data[0]/100))
	wifi.post("pressure",data[1]/256)
	wifi.post("humidity",data[2]/1024)
