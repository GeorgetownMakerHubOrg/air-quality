import sys
import config as constants

# HTTP & Adafruit.io stuff
AIO_KEY = constants.X_AIO_KEY
USER = constants.USER

# NOTE: we could use a module such as `six` to support both Python 2 and Python
# 3, or we could conditionally use libraries after checking `sys.version_info`

if sys.version_info[0] != 2:
    raise Exception("Incorrect Python version; this script is intended to be used with Python 2")

if len(sys.argv) != 2:
    raise Exception("Invalid number of input arguments, please specify Group ID")


def io_post(group):
    import json
    import urllib2

    headers = {"X-AIO-Key": AIO_KEY, "Content-Type": "application/json"}

    url = "https://io.adafruit.com/api/v2/" + USER + "/groups"
    print("URL is:", url)

    data_dict = {"name": group, "description": "Air Quality Monitor - STIA436"}
    data = json.dumps(data_dict).encode('UTF-8')
    print("JSON Payload:", data_dict)

    try:
        req = urllib2.Request(url, data=data, headers=headers)
        response = urllib2.urlopen(req)
        print(response.read())
    except Exception as e:
        # An error will be thrown if the group already exists, or if the
        # maximum number of groups has been reached
        print("Error Posting to IO: {}".format(e))
    else:
        response.close()


print("Setting Group in Adafruit.IO")
io_post(sys.argv[1])
