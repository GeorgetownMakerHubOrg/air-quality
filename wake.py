#
# Code improvement suggestions:
#   1. launch multiple sensor requests to collect simultaneously and place them in the list (threads?)
# measurements = [("temperature", 32), ("humidity", 50), ("pressure", 100)]
# environment = [("voltate", 4.2), ("runtime", 500)]
#   2. *then* wifi connect & post all at once (for i in list...., post())
#   3. sleep
#

def main():
	import machine, utime  # ESP stuff
	from machine import Pin, Signal

	import sleep, bosch, enviro, wifi     # our stuff
	led = Pin(12, Pin.OUT)                # set GPIO12 as output to led
	pin2 = Pin(2, Pin.IN, Pin.PULL_UP)    # set GPIO2 as input with pullup
	button = Signal(pin2, invert=True)    # let's use Signals, eh?

	led.off()
	if machine.reset_cause() == machine.DEEPSLEEP_RESET:
		print('woke from a deep sleep')
		wifi.init_sta(True)
		start_time = utime.ticks_ms()
		bosch.measure()
		enviro.measure(start_time)
		wifi.init_sta(False)
		sleep.init()
	else:
		print('power on or hard reset')
		if button.value():
			print("Enter webREPL and upgrade")
#			wifi.init_sta(False)
#			wifi.init_ap(True)
			led.on()
#			import webrepl 
#			webrepl.start()
#			quit()
		else:
			sleep.init()
