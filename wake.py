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
import config

sleep_interval = config.SLEEP

def sleep(milliseconds):
	"""
	# If this is deployed on ESP8266, uncomment this block
	# to enable real time clock & interrupts for the ESP8266
	# configure RTC.ALARM0 to be able to wake the device
	rtc = machine.RTC()
	rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)

	# set RTC.ALARM0 to fire after X seconds (waking the device)
	rtc.alarm(rtc.ALARM0, milliseconds)
	"""
	# put the device to sleep
	# we'll also need to power off the sensors at some point too.
	machine.deepsleep(milliseconds)

def main():
	import machine, utime, array                         # ESP stuff
	from machine import Pin, Signal
	from sys import exit

	import sleep, iot, stub, tphg, pm25                  # our stuff - comment this line for stub.py

	start_time = utime.ticks_ms()        	             # let's track runtime (for measuring current usage)

	aq = {} 
	id = machine.unique_id()
	chipId='{:02x}{:02x}{:02x}{:02x}'.format(id[0], id[1], id[2], id[3]) # make each sensor its own group

	#aq.update(analog.measure())
	#aq.update(dht11.measure())
	#aq.update(enviro.measure())
	#aq.update(pm25.measure())
	#aq.update(ppd42.measure())
	#aq.update(tph.measure())
	aq.update(tphg.measure())
	#aq.update(stub.measure())	# when you only want the MCU and no sensors.
	# for reasons I can't explain, UART takes time to setup - so do this last? WTF.
	aq.update(pm25.measure())

	iot.init_ap(False)
	iot.init_sta(True)
	# Now let's post all
	
	iot.io_post(chipId,aq)
	#iot.io_post({"runtime": ((utime.ticks_ms() - start_time)/1000)})
	print("Runtime is:", (utime.ticks_ms() - start_time)/1000)
	sleep(sleep_interval)                # see you later!
	
