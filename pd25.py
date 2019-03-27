# Author: F. Pascal Girard
# STIA436 Course - Spring 2019
# Professor Colin McCormick & Father Chris Wagner
#
# credit for the pack/unpack code & variable names goes to ladyada at Adafruit:
# https://learn.adafruit.com/pm25-air-quality-sensor/circuitpython-code


from machine import Pin, UART
from utime import sleep
import pmsa003

uart1=UART(1,rx=0,tx=2,baudrate=9600)
uart2=UART(2,rx=27,tx=26,baudrate=9600)
pd1 = pmsa003.PMSA003(uart1)
pd2 = pmsa003.PMSA003(uart2)

def measure():
	data1 = pd1.read_compensated_data()
	data2 = pd2.read_compensated_data()
	print("Compensated Data 1:", data1)
	print("Compensated Data 2:", data2)
	# Here we should make decisions as to how to combine both sensor data or report both?
	return {  # until i can get more than 10 feeds; can only use 6 for now; 3 from each temporarily
        "pm10-standard":   data1[0],
        "pm25-standard":   data2[1],
        #"pm100-standard":  data1[2],
        "pm10-env":        data1[3],
        "pm25-env":        data2[4],
        #"pm100-env":       data1[5],
        #"particles-03um":  data1[6],
        #"particles-05um":  data1[7],
        "particles-10um":  data1[8],
        "particles-25um":  data2[9],
        #"particles-50um":  data1[10],
        #"particles-100um": data1[11],
        }