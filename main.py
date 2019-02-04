#
# STIA436 Course - Spring 2019
# Professor Colin McCormick & Father Chris Wagner
#
# With support from me, Pascal Girard
#
import utime
from machine import Pin, Signal, Timer

pin0 = Pin(0, Pin.IN, Pin.PULL_UP)   	# set GPIO0 as input with pullup
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
		import webrepl, wifi
		wifi.init_sta(False)
		wifi.init_ap(True)
		webrepl.start()

pin0.irq(trigger=Pin.IRQ_RISING, handler=callback)
timer.init(period=5000, mode=Timer.ONE_SHOT, callback=run)