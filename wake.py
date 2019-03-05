#
# Code improvement suggestions:
#   1. how about one post to submit all new data?  C'mon Adafruit
#
# Don't forget to enable A0 battery as well as sleep (16 & Reset) - solder!
# 
# 
SLEEP = 60

def main():
	import machine, utime, array                         # ESP stuff
	from machine import Pin, Signal
	from sys import exit

	# import sleep, tph, enviro, dht11, analog, wifi    # our stuff
	import sleep, wifi, stub                              # minimum stuff

	start_time = utime.ticks_ms()        	             # let's track runtime (for measuring current usage)

	# data structures for sensors - uses Python's dictionary & lists
	"""aq = [ {'field': 'field1', 'parameter': 'temperature', 'value': '0'},
	       {'field': 'field2', 'parameter': 'humidity', 'value': '0'},
	       {'field': 'field3', 'parameter': 'pressure', 'value': '0'},
	       {'field': 'field4', 'parameter': 'voc', 'value': '0'},
	       {'field': 'field5', 'parameter': 'pm25', 'value': '0'},
	       {'field': 'field6', 'parameter': 'volts', 'value': '0'}]. """

	aq = {'temperature': 0, 'humidity': 0, 'pressure': 0, 'voc': 0, 'A1': 0,'A2': 0,'A3': 0,'volts':0} 
	
	#aq.update(tph.measure())
	#aq.update(tphg.measure())
	#aq.update(ppd42.measure())
	#aq.update(dht11.measure())
	#aq.update(analog.measure())
	#aq.update(enviro.measure())
	aq.update(stub.measure())
	print(aq)
	
	wifi.init_ap(False)
	wifi.init_sta(True)
	# Now let's post all - unfortunately, io.adafruit requires one data post at a time
	for key, value in aq.items():
		wifi.post(key,value)
	wifi.post("runtime", ((utime.ticks_ms() - start_time)/1000))
	sleep.init(SLEEP)                # see you later!
	
