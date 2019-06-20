# GNU General Public License <https://www.gnu.org/licenses>
# STIA436 Course - Spring 2019
# Professor Colin McCormick & Father Chris Wagner
# Copyright (c) 2019 F. Pascal Girard

import machine
from machine import Timer, TouchPad, Pin


TIMER_0 = Timer(0)

# TODO: get values from configuration file
# Touch value is around 500-600 when untouched, and 10-20 when touched
TOUCH_PAD = TouchPad(Pin(14))
TOUCH_THRESHOLD = 50


def run(timer):

    # When the touch value is above the threshold, then it is not being touched
    if TOUCH_PAD.read() > TOUCH_THRESHOLD:
        print("Running sensors...")
        import wake

        wake.main()
    else:
        print("Upgrading...")
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
