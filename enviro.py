# 
# Let's track voltage - enable A0 to voltage on the board by solder.
# What other machine states/conditions do we want to record?
# Using only this module will also allow us to measure current consumption of the ESP without sensor load
#
import machine, micropython
voltage = machine.ADC(0)

def measure():
	return {
        "volts": voltage.read()/230.5
    }
