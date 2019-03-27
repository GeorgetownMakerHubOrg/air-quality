# The MIT License (MIT)
# Copyright (c) F. Pascal Girard
# https://opensource.org/licenses/MIT
# STIA436 Course - Spring 2019
# Professor Colin McCormick & Father Chris Wagner
#
import machine, utime
from machine import Pin, Signal, Timer
"""
# ESP32 Code - see below
# from machine import TouchPad
pad = TouchPad(Pin(14))
"""

timer = Timer(0)
upgrade = False

print('Running main')

def callback(pin):
	global upgrade
	upgrade = True
	return(upgrade)

def run(timer):
	if not upgrade:
		print('Running sensors...')
		import wake
		wake.main()	
	else:
		print('Upgrading...')
		import webrepl, iot
		iot.init_sta(False)
		iot.init_ap(True)
		webrepl.start()

if machine.reset_cause() == machine.DEEPSLEEP_RESET:
	print('Woke from a deep sleep...')
	import wake
	wake.main()

#else:  # an opportunity to enter WebREPL after hard reset
	"""  
	# ESP8266 Code
	pin0 = Pin(0, Pin.IN, Pin.PULL_UP)   	# set GPIO0 as input with pullup
	pin0.irq(trigger=Pin.IRQ_RISING, handler=callback)
	timer.init(period=5000, mode=Timer.ONE_SHOT, callback=run)
	"""
	# ESP32 Code


