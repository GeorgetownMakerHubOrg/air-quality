import machine

def init():
	# configure RTC.ALARM0 to be able to wake the device
	rtc = machine.RTC()
	rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)

	# set RTC.ALARM0 to fire after 10 seconds (waking the device)
	rtc.alarm(rtc.ALARM0, 60000)

	# put the device to sleep
	# power off the sensors too?
	machine.deepsleep()
