# look at: https://tinyurl.com/ychv9wug : 
# By adding a 100k , it will in fact be a total resistance  of 100k+220k+100k=420k.
# So if the Voltage of a fully loaded Cell would be 4.2 Volt, 
# the ADC of the ESP8266 would get 4.2 * 100/420= 1 Volt

import machine
import wifi

def measure():
	adc = machine.ADC(0)
	voltage = adc.get()*4.25/1023
	print('init')
	wifi.init_sta(True)    # minimize antenna power usage
	wifi.post("voltage",voltage)
	print('deinit')
	wifi.init_sta(False)   # turn off antennas?
