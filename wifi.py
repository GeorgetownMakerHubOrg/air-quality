#
# Configure this file by:
# 1. changing the Station, Access Point, and Io.Adafruit.Com Login Information
# 2. renaming this file to "wifi.py"
#
# Geolocation information - format is: ***


import network, utime   # Micropython modules
import sleep, config    # Our modules

# import config constants

# Wifi stuff
sta_ssid = config.STA_SSID
sta_password = config.STA_PASSWORD
ap_ssid = config.AP_SSID
ap_password = config.AP_PASSWORD
sleep_interval = config.SLEEP

# HTTP & Adafruit.io stuff
aio_key = config.X_AIO_KEY
user = config.USER
group = config.GROUP
lat = config.LATITUDE
lon = config.LONGITUDE

# Station object
wlan = network.WLAN(network.STA_IF)

# Access Point object
ap = network.WLAN(network.AP_IF) 

def init_sta(status):
	import utime
	if status == True:
		wlan.active(True)
		count = 0
		if not wlan.isconnected():               # should connect...
			wlan.connect(sta_ssid, sta_password)  # if not then explicitly call connect
			while not wlan.isconnected():        # try connecting for 10 seconds
				print("Waiting for IP... Count:", count)
				if count == 10:
					print ("Can't find wifi - resetting")
					sleep.init(sleep_interval)            # pass an argument to delay awakening?
				utime.sleep(1)
				count +=1 
		print('Network Configuration:', wlan.ifconfig())
	else:
		wlan.active(False)

def init_ap(status):
	if status == True:
		ap.config(essid=ap_ssid, password=ap_password) # set the ESSID & Password
		ap.active(True)                                # BEFORE you activate it
		print('Network Configuration:', ap.ifconfig())
	else:
		ap.active(False)

def post(feed, value):
	import json, urequests
	headers = {'X-AIO-Key': aio_key,'Content-Type': 'application/json'}
	url='https://io.adafruit.com/api/v2/'+user+'/feeds/'+group+'.'+feed+'/data.json'
	# print('URL is:', url)
	data = json.dumps({"value": value, "lat":lat, "lon":lon})
	# POST response
	try:
		response = urequests.post(url, headers=headers, data=data)
	except OSError as err:
		print("OS error: {0}".format(err))
		sleep.init(sleep_interval)
	else:
		response.close()
