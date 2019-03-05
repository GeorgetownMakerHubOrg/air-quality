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
        "pm10_std": 1,
        "pm25_std": 25,
        "pm100_std": 10,
        # PMS-A003 - Concentration Units (environmental)
        "pm10_env": 1,
        "pm25_env": 25,
        "pm100_env": 10,    
        # PMS-A003 - particle count 
        "part_03um": 3,
        "part_05um": 5,
        "part_10um": 10,
        "part_25um": 25,
        "part_50um": 50,
        "part_100um": 100,
        # MCU variables
        "volts": 3.3
    }