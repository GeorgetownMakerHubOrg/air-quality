# GNU General Public License <https://www.gnu.org/licenses>
# STIA436 Course - Spring 2019
# Professor Colin McCormick & Father Chris Wagner
# Copyright (c) 2019 F. Pascal Girard
#

import network
import sleep
import config

# Wifi stuff
sta_ssid = config.STA_SSID
sta_password = config.STA_PASSWORD
ap_ssid = config.AP_SSID
ap_password = config.AP_PASSWORD
sleep_interval = config.SLEEP

# HTTP & Adafruit.io stuff
aio_key = config.X_AIO_KEY
user = config.USER
lat = config.LATITUDE
lon = config.LONGITUDE

# Network objects
wlan = network.WLAN(network.STA_IF)
ap = network.WLAN(network.AP_IF)


def init_sta(status):
    import utime

    if status:
        wlan.active(True)
        count = 0
        if not wlan.isconnected():                # should connect...
            wlan.connect(sta_ssid, sta_password)  # if not then explicitly call connect
            while not wlan.isconnected():         # try connecting for 10 seconds
                print("Waiting for IP... Count:", count)
                if count == 10:
                    print("Can't find wifi - resetting")
                    sleep.init(sleep_interval)    # pass an argument to delay awakening?
                utime.sleep(1)
                count += 1
        print("Network Configuration:", wlan.ifconfig())
    else:
        wlan.active(False)


def init_ap(status):
    if status:
        ap.config(essid=ap_ssid, password=ap_password)  # set the ESSID & Password
        ap.active(True)                                 # BEFORE you activate it
        print("Network Configuration:", ap.ifconfig())
    else:
        ap.active(False)


def io_post(group, aq):
    """POST air quality metrics to Adafruit I/O

    :param group:  topic group for data feed
    :param aq: dictionary of sensor measurements
    """
    import json
    import sleep
    import urequests

    headers = {"X-AIO-Key": aio_key, "Content-Type": "application/json"}
    url = "https://io.adafruit.com/api/v2/" + user + "/groups/" + group + "/data"
    print("URL is:", url)
    aqlist = []
    for key, value in aq.items():
        aqlist.append({"key": key, "value": value})
    api_list = {"location": {"lat": lat, "lon": lon}, "feeds": aqlist}
    data = json.dumps(api_list)

    try:
        response = urequests.post(url, headers=headers, data=data)
        print(response.text)
    except OSError as e:
        print("OS error: {0}".format(e))
        sleep.init(sleep_interval)
    except IndexError as e:
        # This should not occur if we ensure that we are connected to the
        # wireless network...
        # See: https://github.com/micropython/micropython-lib/issues/300
        print("Index Error using urequests: {0}".format(e))
        sleep.init(sleep_interval)
    else:
        response.close()
