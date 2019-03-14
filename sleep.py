import machine

def init(seconds):
	"""
	# If this is deployed on ESP8266, uncomment this block
	# to enable real time clock & interrupts for the ESP8266
	# configure RTC.ALARM0 to be able to wake the device
	rtc = machine.RTC()
	rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)

	# set RTC.ALARM0 to fire after X seconds (waking the device)
	rtc.alarm(rtc.ALARM0, seconds*1000)
	"""
	# put the device to sleep
	# we'll also need to power off the sensors at some point too.
	machine.deepsleep(seconds)