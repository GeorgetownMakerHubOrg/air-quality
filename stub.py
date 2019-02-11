# 
# A stub sensor so we can test the core code without sensors
# This will also allow us to measure current consumption of the ESP without sensor load
#

def measure():
	return {
        "volts": 3.3,
        "temperature": 32,
        "humidity": 80,
        "pressure": 100000,
        "A0": 3261,    
        "A1": 3262,
        "A2": 3263,
        "A3": 3264
    }