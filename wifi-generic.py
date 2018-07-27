#
# Configure this file by:
# 1. changing the Station, Access Point, and Io.Adafruit.Com Login Information
# 2. renaming this file to "wifi.py"
#
STA_SSID = 'My-Wifi- SSID'
STA_Password = 'asdf4r123'
AP_SSID = 'STIA315'
AP_Password = 'sasdf4r23'
User = 'fpgirard'
X_AIO_Key = '025adsfasdfasdfkqwerasdfasdfb199c42f4520'

import network
import sleep
wlan = network.WLAN(network.STA_IF)

# Access Point Variables

ap = network.WLAN(network.AP_IF) 

def init_sta(status):
	if status == True:
		wlan.active(True)
		if not wlan.isconnected():
			print('Connecting To Network...') 
			wlan.connect(STA_SSID, STA_Password)
			# this might chew up the battery ... change to 10 attempts?
			while not wlan.isconnected():
				pass
		print('Network Configuration:', wlan.ifconfig())
	else:
		wlan.active(False)

def post(Feed, value):
	import json, urequests
	headers = {'X-AIO-Key': X_AIO_Key,'Content-Type': 'application/json'}
	url='https://io.adafruit.com/api/v2/'+User+'/feeds/hub.'+Feed+'/data.json'
	data = json.dumps({"value": value})
	# POST response
	try:
		response = urequests.post(url, headers=headers, data=data)
	except OSError as err:
		print("OS error: {0}".format(err))
		sleep.init()
	else:
		response.close()

def init_ap(status):
	if status == True:
		print('activate AP_SSID')
		ap.active(True)         
		ap.config(essid=AP_SSID, password=AP_Password) # set the ESSID of the access point
	else:
		print('deactivate Access Point')
		ap.active(False)
