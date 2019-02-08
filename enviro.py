# 
# Let's track voltage - enable A0 to voltage on the board by solder.
#
import machine, micropython
voltage = machine.ADC(0)

def measure(v):
	v[0] = voltage.read()/230.5     # 975/4.25
	print ("voltage is:", v[0])
	print ("memory usage is: ", micropython.mem_info())
	return(v)
