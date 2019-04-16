# The MIT License (MIT) - https://opensource.org/licenses/MIT
# STIA436 Course - Spring 2019
# Professor Colin McCormick & Father Chris Wagner
# F. Pascal Girard
#
# Code improvement suggestions:
#   1. how about one post to submit all new data?  C'mon Adafruit
#
# Don't forget to enable A0 battery as well as sleep (16 & Reset) - solder!
# 
# 
from utilities import config
import machine 
import sleep

sleep_interval = config.SLEEP

def main():
	import utime, array                         # ESP stuff
	from machine import Pin, Signal
	from sys import exit

	# import tphg, pm25             			# our sensors - comment this line for stub.py
	import stub									# when no sensors are attached.
	import iot		          					# IOT networking
	start_time = utime.ticks_ms()				# let's track runtime (for measuring current usage)

	aq = {} 
	id = machine.unique_id()
	chipId='{:02x}{:02x}{:02x}{:02x}{:02x}{:02x}'.format(id[0], id[1], id[2], id[3], id[4], id[5]) # make each sensor its own group

	#aq.update(analog.measure())
	#aq.update(dht11.measure())
	#aq.update(enviro.measure())
	#aq.update(pm25.measure())
	#aq.update(ppd42.measure())
	#aq.update(tph.measure())
	#aq.update(tphg.measure())
	aq.update(stub.measure())	# when you only want the MCU and no sensors.
	# for reasons I can't explain, UART takes time to setup - so do this last? WTF.
	#aq.update(pm25.measure())

	iot.init_ap(False)
	iot.init_sta(True)
	# Now let's post all
	
	iot.io_post(chipId,aq)
	#iot.io_post({"runtime": ((utime.ticks_ms() - start_time)/1000)})
	print("Runtime is:", (utime.ticks_ms() - start_time)/1000)
	sleep.init(sleep_interval)                # see you later!
	
