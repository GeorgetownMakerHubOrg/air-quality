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

	import sleep, tph280, enviro, dht11, analog, wifi    # our stuff

	start_time = utime.ticks_ms()        	             # let's track runtime (for measuring current usage)

	# data structures for sensors - uses Python's Dictionary & Lists
	aq = {'temperature': 0, 'humidity': 0, 'pressure': 0, 'voc': 0, 'A1': 0,'A2': 0,'A3': 0,'volts':0} 
	
	aq.update(tph280.measure())
	#aq.update(tphg680.measure())
	aq.update(dht11.measure())
	aq.update(analog.measure())
	aq.update(enviro.measure())

	wifi.init_ap(False)
	wifi.init_sta(True)
	# Now let's post all - unfortunately, io.adafruit requires one data post at a time
	for key, value in aq.items():
		wifi.post(key,value)
		wifi.post("runtime", ((utime.ticks_ms() - start_time)/1000))
	sleep.init(SLEEP)                # see you later!
	