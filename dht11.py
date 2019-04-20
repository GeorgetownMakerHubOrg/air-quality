# GNU General Public License <https://www.gnu.org/licenses>
# STIA436 Course - Spring 2019
# Professor Colin McCormick & Father Chris Wagner
# Copyright (c) 2019 F. Pascal Girard

import dht
from machine import Pin
# select a digital pin on the ESP
data = dht.DHT11(Pin(2))

def measure():
	data.measure()
	return {
        "temperature": data.temperature(), 
        "humidity": data.humidity()
    }
	
