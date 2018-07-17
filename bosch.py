# from: https://github.com/shaoziyang/mpy-lib/blob/master/sensor/bmp280/bmp280.py
#import machine
from machine import I2C, Pin   # create an I2C bus object for BMP180 sensor
import wifi, bmp280

def to_F(value):
	return(value*(9/5)+32)

def measure():
	b = bmp280.BMP280(I2C(scl=Pin(5), sda=Pin(4)))
	print('calling get')
	b.get()
	print('wifi init')
	wifi.init()    # minimize antenna power usage
	print('wifi post1')
	wifi.post("bmp-temperature",to_F(b.T))
	print('wifi post2')
	wifi.post("pressure",b.P)
	print('deinit')
	wifi.deinit()   # turn off antennas?
	print('leaving bosch - bye!')
