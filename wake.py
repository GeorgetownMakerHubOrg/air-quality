#
# Code improvement suggestions:
#   1. launch multiple sensor requests to collect simultaneously and place them in the list (threads?)
#   2. *then* wifi connect & post all at once (for i in list...., post())
#   3. sleep
#

def main():
	import machine, utime, array          # ESP stuff
	from machine import Pin, Signal
	from sys import exit

	import sleep, bosch, enviro, wifi     # our stuff

	start_time = utime.ticks_ms()         # let's track runtime (for measuring current usage)
	led = Pin(12, Pin.OUT)                # set GPIO12 as output to led
	pin2 = Pin(2, Pin.IN, Pin.PULL_UP)    # set GPIO2 as input with pullup
	button = Signal(pin2, invert=True)    # let's use Signals, eh?

	# create numeric arrays for each sensor
	tph = array.array('f',[0., 0., 0.])   # BME280 Temp, Press, & Humid.
	v = array.array('f',[0.])              # Voltage
	
	led.off()
	if machine.reset_cause() == machine.DEEPSLEEP_RESET:
		print('woke from a deep sleep')
		tph = bosch.measure(tph)
		v = enviro.measure(v)
		# Now let's post all
		wifi.init_sta(True)
		wifi.post("temperature",tph[0])  # in F
		wifi.post("pressure",tph[1])     # in kPa
		wifi.post("humidity",tph[2])     # in %
		wifi.post("runtime", ((utime.ticks_ms() - start_time)/1000))
		wifi.post("voltage",v[0])
		#wifi.init_sta(False)
		sleep.init(600)                  # see you later!
	else:
		print('power on or hard reset')
		if button.value():
			print("Enter webREPL and upgrade")
			wifi.init_sta(False)
			wifi.init_ap(True)
#			led.on()
			import webrepl 
			webrepl.start()
			exit()
		else:
			sleep.init(600)
