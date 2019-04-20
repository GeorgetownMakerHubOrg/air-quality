# GNU General Public License <https://www.gnu.org/licenses>
# STIA436 Course - Spring 2019
# Professor Colin McCormick & Father Chris Wagner
# Copyright (c) 2019 F. Pascal Girard
#
# Configure this file by:
# 1. changing the Station, Access Point, and Io.Adafruit.Com Login Information
# 2. renaming this file to "config.py"
#
# Geolocation information - default on Carroll's statue: lat=38.907606, lon=-77.072257

LATITUDE = 38.907606
LONGITUDE = -77.072257

#Wifi Parameters
STA_SSID = 'GuestNet'
STA_PASSWORD = 'GoHoyaSaxa'
AP_SSID = 'STIA436-fpg'				# use an SSID that combines class and GUid to make it unique.
AP_PASSWORD = 'HillTopHoyas'

# Adafruit
X_AIO_KEY = 'Io.Adafruit.X_AIO_KEY025ea3251b199c42f4520'
USER = 'IO-ADAFRUIT-USER-NAME'
GROUP = 'Adafruit-Group-Name'
# ThingSpeak - Write API Key
TS_KEY = 'THINGSPEAKWRITEKEY'

# Sleep time for wake/sleep cycle in milliseconds
SLEEP = 60*1000