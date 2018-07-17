#
# Code improvement suggestions:
#   1. launch multiple sensor requests to collect simultaneously and place them in the list (threads?)
#   2. *then* wifi connect & post all at once (for i in list...., post())
#   3. sleep
#
import machine               # ESP stuff
from machine import Pin, Signal

import sleep, bosch, wifi  # our stuff
pin12 = Pin(12, Pin.IN, Pin.PULL_UP)   # set GPIO12 as input with pullup
button = Signal(pin12, invert=True)   # let's use Signals, eh?

if machine.reset_cause() == machine.DEEPSLEEP_RESET:
	print('woke from a deep sleep')
	bosch.measure()
	print('calling sleep.init from reset')
	sleep.init()
else:
	print('power on or hard reset')
	if button.value():
		print("Enter webREPL and upgrade")
		# wifi.ap('Pascal')
		# webREPL enable
		# quit()
	else:
		print('calling sleep.init from power on')
		sleep.init()
