# Author: Pascal Girard
#
# Tool to set adafruit.io group for this ESP MCU
#import machine
import config as constants

# HTTP & Adafruit.io stuff
aio_key = constants.X_AIO_KEY
user = constants.USER

def io_post(group):
	import json, requests
	headers = {'X-AIO-Key': aio_key,'Content-Type': 'application/json'}
	url='https://io.adafruit.com/api/v2/'+user+'/groups'
	# url='https://io.adafruit.com/api/v2/'+user+'/feeds/'+group+'.'+feed+'/data.json'
	print('URL is:', url)
	mystr = {"name":group, "description":"A collection of feeds", "visibility":"public"}
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

#id = machine.unique_id()
#chipId='{:02x}{:02x}{:02x}{:02x}'.format(id[0], id[1], id[2], id[3]) # make each sensor its own group
io_post('3c71bf0a')
