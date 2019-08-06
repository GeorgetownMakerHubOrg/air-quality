from __future__ import print_function

import json
import sys

import config as constants

# Conditionally import `urllib` to work with Python 2 & 3
if sys.version_info[0] == 3:
    from urllib.request import urlopen, Request
else:
    from urllib2 import urlopen, Request


def io_post(group):
    """
    Post device ID to Adafruit IO to register group

    @param group: Group ID for the device
    """

    headers = {"X-AIO-Key": constants.X_AIO_KEY, "Content-Type": "application/json"}

    url = "https://io.adafruit.com/api/v2/" + constants.USER + "/groups"
    print("URL is:", url)

    data_dict = {"name": group, "description": "Air Quality Monitor - STIA436"}
    data = json.dumps(data_dict).encode('UTF-8')
    print("JSON Payload:", data_dict)

    try:
        req = Request(url, data=data, headers=headers)
        response = urlopen(req)
        print(response.read())
    except Exception as e:
        # An error will be thrown if the group already exists, or if the
        # maximum number of groups has been reached
        print("Error Posting to IO: {}".format(e))
    else:
        response.close()


if __name__ == "__main__":

    if len(sys.argv) != 2:
        raise Exception("Invalid number of input arguments, please specify Group ID")

    print("Setting Group in Adafruit.IO")
    io_post(sys.argv[1])

