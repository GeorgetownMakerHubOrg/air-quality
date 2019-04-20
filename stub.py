# GNU General Public License <https://www.gnu.org/licenses>
# STIA436 Course - Spring 2019
# Professor Colin McCormick & Father Chris Wagner
# Copyright (c) 2019 F. Pascal Girard

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
        "voc": 256000,
        "pm10-standard": 10,
        "pm25-standard": 25,
        "pm100-standard": 100,
        "pm10-env": 10,
        "pm25-env": 25,
        "pm100-env": 100,
        "particles-03um": 3,
        "particles-05um": 5,
        "particles-10um": 10,
        "particles-25um": 25,
        "particles-50um": 50,
        "particles-100um": 100
        }