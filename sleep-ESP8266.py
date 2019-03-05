#
# If you're planning to use an ESP8266, rename this file to sleep.py
# 
import machine

def init(seconds):
	# configure RTC.ALARM0 to be able to wake the device
	rtc = machine.RTC()
	rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)

	# set RTC.ALARM0 to fire after X seconds (waking the device)
	rtc.alarm(rtc.ALARM0, seconds*1000)

	# put the device to sleep
	# power off the sensors too?
	machine.deepsleep()
