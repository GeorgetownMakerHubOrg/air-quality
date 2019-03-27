# The MIT License (MIT)
# Copyright (c) F. Pascal Girard
# https://opensource.org/licenses/MIT
# STIA436 Course - Spring 2019
# Professor Colin McCormick & Father Chris Wagner
# 
# A stub sensor so we can test the core code without sensors
# This will also allow us to measure current consumption of the ESP without sensor load
#

def measure():
	return {
        # BME680 
        "temperature": 32,
        "humidity": 80,
        "pressure": 100000,
        "voc": 80,
        # PMS-A003 - Concentration Units (standard)
        "pm10-std": 1,
        "pm25-std": 25,
        "pm100-std": 10,
        # PMS-A003 - Concentration Units (environmental)
        "pm10-env": 1,
        "pm25-env": 25,
        "pm100-env": 10,    
        # PMS-A003 - Particle Count 
        "part-03um": 3,
        "part-05um": 5,
        "part-10um": 10,
        "part-25um": 25,
        "part-50um": 50,
        "part-100um": 100,
        # MCU variables
        "volts": 3.3
    }