#
# Code improvement suggestions:
#   1. how about one post to submit all new data?  C'mon Adafruit
#
# Don't forget to enable A0 battery as well as sleep (16 & Reset) - solder!
# 
# 

def main():
	import machine, utime, array          # ESP stuff
	from machine import Pin, Signal
	from sys import exit

	import sleep, tph280, enviro, analog, wifi    # our stuff

	start_time = utime.ticks_ms()             # let's track runtime (for measuring current usage)
	# device stuff 

	pin2 = Pin(2, Pin.IN, Pin.PULL_UP)        # set GPIO0 as input with pullup for upgrading via WebREPL
	button = Signal(pin2, invert=True)        # let's use Signals, eh?

	# create numeric arrays for each sensor
	tph = array.array('f',[0., 0., 0.])   # BME280 Temp, Press, & Humid
	tphg = array.array('f',[0.,0.,0.,0.]) # BME680 Temp, Press, Humid, and Gas
	adc = array.array('i',[0,0,0,0])
	v = array.array('f',[0.])             # Voltage
	
	if machine.reset_cause() == machine.DEEPSLEEP_RESET:
		print('woke from a deep sleep')
		tph = tph280.measure(tph)
		#tphg = b680.measure(tphg) """fix this"""
		adc = analog.measure(adc)
		v = enviro.measure(v)
		# Now let's post all - unfortunately, io.adafruit requires one data post at a time
		wifi.init_ap(False)
		wifi.init_sta(True)
		wifi.post("temperature",tph[0])  # in F
		wifi.post("pressure",tph[1])     # in kPa
		wifi.post("humidity",tph[2])     # in %
		wifi.post("a0",adc[0])           # Analog 0
		wifi.post("a1",adc[1])           # Analog 1
		wifi.post("a2",adc[2])           # Analog 2
		wifi.post("a3",adc[3])           # Analog 3
		wifi.post("voltage",v[0])
		wifi.post("runtime", ((utime.ticks_ms() - start_time)/1000))
		sleep.init(5)                    # see you later!
	else:
		print('power on or hard reset')
		if button.value():
			print("Enter webREPL and upgrade")
			wifi.init_sta(False)
			wifi.init_ap(True)
			import webrepl 
			webrepl.start()
			exit()
		else:
			sleep.init(10)