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
        # PMS-A003 - Concentration Units (standard)
        "pm25-std": 25,
        # PMS-A003 - Concentration Units (environmental)
        "pm25-env": 25,  
        # PMS-A003 - Particle Count 
        "part-25um": 25
        }