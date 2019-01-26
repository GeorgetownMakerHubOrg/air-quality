#
# BME680 code from ***
# Given that we might have multiple Bosch sensors on I2C bus, we might have to alter the
# BME680 default address (0x77)
# 
# Do we want to use median() to take multiple samples to remove noise?

import array
#from machine import I2C, Pin   # create an I2C bus object for all I2C-based sensors.

"""import bme680
i2c = I2C(scl=Pin(5), sda=Pin(4))		       # create the I2C bus
bme680 = bme680.BME680(i2c=i2c, address=0x77)

def measure(tphg):
	print("BME 680 Values:", bme280.values)
	raw = bme280.read_compensated_data()
	tph[0] = (raw[0]/100.)*(9/5)+32  # Fahrenheit  
	tph[1] = raw[1]/(256*1000.)      # kPa
	tph[2] = raw[2]/1024.            # % 
	return(tph). """