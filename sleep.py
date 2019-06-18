# GNU General Public License <https://www.gnu.org/licenses>
# STIA436 Course - Spring 2019
# Professor Colin McCormick & Father Chris Wagner
# Copyright (c) 2019 F. Pascal Girard


def init(milliseconds):
    import machine

    """
    # If this is deployed on ESP8266, uncomment this block
    # to enable real time clock & interrupts for the ESP8266
    # configure RTC.ALARM0 to be able to wake the device
    rtc = machine.RTC()
    rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)

    # set RTC.ALARM0 to fire after X seconds (waking the device)
    rtc.alarm(rtc.ALARM0, milliseconds)
    """
    # put the device to sleep
    # we'll also need to power off the sensors at some point too.
    machine.deepsleep(milliseconds)
