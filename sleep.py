import machine

def init(seconds):
	# put the device to sleep
	# power off the sensors too?
	machine.deepsleep(seconds)
