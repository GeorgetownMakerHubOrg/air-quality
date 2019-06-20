# GNU General Public License <https://www.gnu.org/licenses>
# STIA436 Course - Spring 2019
# Professor Colin McCormick & Father Chris Wagner
# Copyright (c) 2019 F. Pascal Girard
#
# Let's track voltage - enable A0 to voltage on the board by solder.
# What other machine states/conditions do we want to record?
# Using only this module will also allow us to measure current consumption of the ESP without sensor load
#

import machine
from machine import Pin

voltage = machine.ADC(Pin(0))


def measure():
    return {
        "volts": voltage.read() / 230.5
    }
