# might want to check for OS error on urequest line
SSID = 'Girards'
Password = 'sadfadf23'
X_AIO_Key = '025ea32223234980888uyadf77y1b199c42f4520'
User = 'fpgirard'

import network
import sleep
wlan = network.WLAN(network.STA_IF)

def init():
	wlan.active(True)
	if not wlan.isconnected():
		print('connecting to network...')
		wlan.connect(SSID, Password)
		while not wlan.isconnected():
			pass
	print('Network Configuration:', wlan.ifconfig())

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

def deinit():
	wlan.active(False)
