#
# Code improvement suggestions:
#   1. how about one post to submit all new data?  C'mon Adafruit
#
# Don't forget to enable A0 battery as well as sleep (16 & Reset) - solder!
# 
# 
import config

sleep_interval = config.SLEEP

def main():
	import machine, utime, array                         # ESP stuff
	from machine import Pin, Signal
	from sys import exit

	# import sleep, tph, enviro, dht11, analog, iot    # our stuff
	import sleep, iot, stub, tphg                      # our stuff

	start_time = utime.ticks_ms()        	             # let's track runtime (for measuring current usage)

	# data structures for sensors - uses Python's dictionary & lists
	"""aq = [ {'field': 'field1', 'parameter': 'temperature', 'value': '0'},
	       {'field': 'field2', 'parameter': 'humidity', 'value': '0'},
	       {'field': 'field3', 'parameter': 'pressure', 'value': '0'},
	       {'field': 'field4', 'parameter': 'voc', 'value': '0'},
	       {'field': 'field5', 'parameter': 'pm25', 'value': '0'},
	       {'field': 'field6', 'parameter': 'volts', 'value': '0'}]. """

	aq = {} 
	
	#aq.update(tph.measure())
	aq.update(tphg.measure())
	#aq.update(ppd42.measure())
	#aq.update(dht11.measure())
	#aq.update(analog.measure())
	#aq.update(enviro.measure())
	#aq.update(stub.measure())
	print(aq)
	
	iot.init_ap(False)
	iot.init_sta(True)
	# Now let's post all - unfortunately, io.adafruit requires one data post at a time
	for key, value in aq.items():
		iot.post(key,value)
	iot.post("runtime", ((utime.ticks_ms() - start_time)/1000))
	sleep.init(sleep_interval)                # see you later!
	
