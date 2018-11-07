# from: https://github.com/shaoziyang/mpy-lib/blob/master/sensor/bmp280/bmp280.py
import machine, micropython, utime
import wifi
voltage = machine.ADC(0)

def measure(v):
	v[0] = voltage.read()/230.5     # 975/4.25
	print ("voltage is:", v[0])
	print ("memory usage is: ", micropython.mem_info())
	return(v)
