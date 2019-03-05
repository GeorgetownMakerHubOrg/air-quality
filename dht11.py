import dht
from machine import Pin
data = dht.DHT11(Pin(2))

def measure():
	data.measure()
	return {
        "temperature": data.temperature(), 
        "humidity": data.humidity()
    }
	
