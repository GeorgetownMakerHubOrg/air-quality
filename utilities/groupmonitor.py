# Author: Pascal Girard
#
# Tool to set adafruit.io group for this ESP MCU
import config as constants

# HTTP & Adafruit.io stuff
aio_key = constants.X_AIO_KEY
user = constants.USER
group = {"deadbeef"}

def io_post(group, aq):
	import json, requests
	headers = {'X-AIO-Key': aio_key,'Content-Type': 'application/json'}
	url='https://io.adafruit.com/api/v2/'+user+'/groups/'
	# url='https://io.adafruit.com/api/v2/'+user+'/feeds/'+group+'.'+feed+'/data.json'
	print('URL is:', url)
	mylist = []
	for key, value in aq.items():
		print('K/V:', key, value)
		mylist.append({"key": key, "value": value})
	print("Mylist", mylist)
	mystr = {"name":"deadbeef", "description":"Pascal collection of feeds"}
	#mystr = { "location": {"lat": lat, "lon": lon}, "feeds": mylist}
	print("Mystr:", mystr)
	data = json.dumps(mystr)
	# POST response
	try:
		response = requests.post(url, headers=headers, data=data)
		print(response.text)
	except OSError as err:
		print("OS error: {0}".format(err))
		sleep.init(sleep_interval)
	else:
		response.close()

def main():
	mylist = {"temperature": 100, "humidity": 20, "pressure": 1000}
	print(mylist)
	io_post(group, mylist)