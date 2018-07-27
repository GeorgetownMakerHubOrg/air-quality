# from: https://github.com/shaoziyang/mpy-lib/blob/master/sensor/bmp280/bmp280.py
import machine, micropython, utime
import wifi
voltage = machine.ADC(0)

def measure(start_time):
	print ("voltage is:", voltage.read())
	print ("memory usage is: ", micropython.mem_info())
	wifi.post("runtime", ((utime.ticks_ms() - start_time)/1000))
	wifi.post("voltage", voltage.read())
