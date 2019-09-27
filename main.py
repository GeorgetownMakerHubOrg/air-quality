# GNU General Public License <https://www.gnu.org/licenses>
# STIA436 Course - Spring 2019
# Professor Colin McCormick & Father Chris Wagner
# Copyright (c) 2019 F. Pascal Girard

import machine
from machine import Timer, TouchPad, Pin, Signal
from config import TOUCH_PIN, TOUCH_THRESHOLD

TIMER_0 = Timer(0)
TOUCH_PAD = TouchPad(Pin(TOUCH_PIN))

led = Pin(5, Pin.OUT, value=1)
blue_led = Signal(led, invert=True)

def run(timer):

    touch_value = TOUCH_PAD.read()
    print("Touch Value: {}, Touch Threshold {}".format(touch_value, TOUCH_THRESHOLD))

    # When the touch value is above the threshold, then it is not being touched
    if touch_value > TOUCH_THRESHOLD:
        print("Running Sensors...")
        import wake
        wake.main()
    else:
        print("Starting AP and Web REPL...")
        blue_led.on()
        import webrepl
        import iot
        iot.init_sta(False)
        iot.init_ap(True)
        webrepl.start()


if machine.reset_cause() == machine.DEEPSLEEP_RESET:
    print("Woke from a deep sleep...")
    import wake

    wake.main()

else:  # an opportunity to enter WebREPL after hard reset
    print("Hard reset")
    TIMER_0.init(period=5000, mode=Timer.ONE_SHOT, callback=run)
