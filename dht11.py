import dht
from machine import Pin
d = dht.DHT11(Pin(2))

def measure(ht):
	d.measure()
	ht[0] = d.temperature()
	ht[1] = d.humidity()
	print ("temperature is:", ht[0])
	print ("humidity is: ", ht[1])
	return(ht)