#
# Configure this file by:
# 1. changing the Station, Access Point, and Io.Adafruit.Com Login Information
# 2. renaming this file to "wifi.py"
#
STA_SSID = 'GuestNet'
STA_Password = 'GoHoyaSaxa'
AP_SSID = 'STIA436-fpg'				# use an SSID that combines class and GUid to make it unique.
AP_Password = 'HillTopHoyas'
X_AIO_Key = 'Io.Adafruit.X_AIO_KEY025ea3251b199c42f4520'
User = 'IO-ADAFRUIT-USER-NAME'
Group = 'stia436'

SLEEP = 5
import network
import sleep

# Station 
wlan = network.WLAN(network.STA_IF)

# Access Point Variables
ap = network.WLAN(network.AP_IF) 

def init_sta(status):
	import utime
	if status == True:
		wlan.active(True)
		count = 0
		if not wlan.isconnected():               # should connect...
			wlan.connect(STA_SSID,STA_Password)  # if not then explicitly call connect
			while not wlan.isconnected():        # try connecting for 10 seconds
				print("Waiting for IP... Count:", count)
				if count == 10:
					print ("Can't find wifi - resetting")
					sleep.init(SLEEP)            # pass an argument to delay awakening?
				utime.sleep(1)
				count +=1 
		print('Network Configuration:', wlan.ifconfig())
	else:
		wlan.active(False)

def init_ap(status):
	if status == True:
		ap.config(essid=AP_SSID, password=AP_Password) # set the ESSID & Password
		ap.active(True)                                # BEFORE you activate it
		print('Network Configuration:', ap.ifconfig())
	else:
		ap.active(False)

def post(Feed, value):
	import json, urequests
	headers = {'X-AIO-Key': X_AIO_Key,'Content-Type': 'application/json'}
	url='https://io.adafruit.com/api/v2/'+User+'/feeds/'+Group+'.'+Feed+'/data.json'
	# print('URL is:', url)
	data = json.dumps({"value": value})
	# POST response
	try:
		response = urequests.post(url, headers=headers, data=data)
	except OSError as err:
		print("OS error: {0}".format(err))
		sleep.init(SLEEP)
	else:
		response.close()