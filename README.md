# STIA 436 - Air Quality Innovation

![alt text](https://github.com/GeorgetownMakerHubOrg/air-quality/blob/master/static/Layla-905.jpg)

## Improvements on the [STIA315](https://github.com/colinmccormick/Georgetown_STIA315_AQ_monitor) course.   

These include:

1. Code written in Micropython
1. Integrated battery shield and Expressif ESP32 WROOM-32 circuitry on single board (Lolin D32)
1. Stevenson case to improve air flow
1. Crisp wiring that leverages the I2C bus
1. Full deep-sleep & wake cycling
1. Significant cost reduction (66% reduction)
1. Lithium Ion Battery with 20% greater mAh at 87% cost savings over LiPo
1. Optional four (4) 16bit Analog Channels for ADC sensors
1. Voltage monitoring on a ADC channel

## Prototype Components

The prototype has the following components:

1. [LOLIN D32 ESP32 Board ](https://wiki.wemos.cc/products:d32:d32)
1. [Stevenson enclosure from Acurite](https://tinyurl.com/y52xd67g)
1. I2C-based Sensors:
	- [BME280 sensor (Temperature, Pressure, Humidity)](https://tinyurl.com/yafl3h9x)
	- [BME680 sensor (Temperature, Pressure, Humidity, and Carbon-based Gas Particles)](https://www.bosch-sensortec.com/bst/products/all_products/bme680)
1. Two (2) Plantower [PMS-A003 Particle Sensors](https://datasheet.lcsc.com/szlcsc/Beijing-Plantower-PMSA003-A_C132744.pdf)
1. Optional [USB connected Solar Panel](https://tinyurl.com/yad7xpcu)
1. [Optional 3000mAh 18650 Lithium Ion Battery](https://www.ebay.com/itm/202512035904)

## Open Actions/Areas of Investigation & Improvement:

1. This repo has migrated to the ESP32 MCU.   There are minor implementation differences that we'll need to manage through (eg. sleep or upgrade method).
1. Better understanding of the accuracy and target purpose of the PMS-A003 and Bosch BME680 Sensors. [Super interesting paper](https://uwspace.uwaterloo.ca/bitstream/handle/10012/12776/Tan_Ben.pdf?sequence=5) on the Plantower sensors. We're on the right track with our sensors - check [this](https://seetheair.wordpress.com/2019/01/15/review-purpleair-ii/) out.
1. Integration with other IoT sites - ThingSpeak, Wunderground.  As a class, we also need to come to some resolution as to how we want to integrate the collection of data from multiple sites.  Does each site have its own IOT service?   Do we have a single IOT account and assign each sensor to be its own channel (thingspeak) or group (adafruit.io)?   The latter would require that we share a single API key with all interested parties.  Might not be a bad thing to do since we're collecting non-sensitive, non-critical data over the past 60 days. 
1. More and more articles are appearing on this subject of Consumer Grade Air Quality Monitoring such as [this](https://molekule.com/blog/consumer-grade-air-quality-sensors-are-they-good-enough/).  [Volatile Organic Compounds](https://toxtown.nlm.nih.gov/chemicals-and-contaminants/volatile-organic-compounds-vocs) are nasty!  A [decent listing of AQ sensors](https://aqicn.org/sensor/) is, of course, in China.   A [DIY site](https://www.byteyourlife.com/en/household-tools/particulate-matter-sensor-controller-project-luftdaten-info/7204) where you can register your device.
1. Continue to evaluate power usage using the DC Power Supply in the Hub. Are sensors unnecessarily draining the battery? 
1. Let's track low power options like [nanoPower](http://nanopower.no/#p) which uses the nrf chipset from Norway.
1. More details on this monitor's design and roadmap are described in this [Google document](https://docs.google.com/document/d/1_XBc5c5FSMccZlWRLiqR3a8eLAP81eoLvET66j237zA).

## Data Collection choices:

Why Adafruit.IO is arguably better than ThingSpeak:

    - Great documentation
	- Solid REST & MQTT support
	- You can download all data from the push of one button
	- Fields can be set up as Key/Value pairs e.g "Temperature", 32
	- You can create fields on the fly
	- You can create groups (monitors) on the fly
	- You can set alerts using IFTTT webhooks to alert for events (high particulate matter sensor readings when battery hits a threshold).

## Notes

* You will need the following tools with this project:

	1. [esptool.py](https://github.com/espressif/esptool) - for flashing MicroPython on the ESP32 Lolin/Wemos Pro
	1. [ampy](https://github.com/pycampers/ampy) - for uploading/downloading/list files to/from the ESP32.
	1. [MicroPython](https://github.com/micropython) - if you're up for building from source!
	1. [WebREPL files](https://github.com/micropython/webrepl) to access the ESP wirelessly

* The "utilities" directory contains the following scripts and executables for:

	1. Basic hardware testing to ensure that sensors are properly connected and minimally operating (hwtest.py)
	1. Confirming that connectivity to Adafruit IO is working properly (to be run on a laptop running Python) (testiot.py)
	1. Automatically creating an Adafruit IO group unique to each monitor (setgroup.py) 
	1. Installing Micropython binary v. 1.10 for the ESP32 using esptool.py (esp32-[version].bin
	1. Building an ESP with all the necessary AQ module and installing micropython from scratch (upload). Be sure to rename the file main\~.py to main.py - this is done so that you can access the ESP32 and do minor testing via the REPL interface before main.py automatically runs the AQ code on boot up.

* This code base leverages several other important MicroPython repositories including but not limited to:
	* [BME280 Repo](https://github.com/catdog2/mpy_bme280_esp8266) - 
	* [Pimoroni BME680 Repo](https://github.com/pimoroni/bme680-python) - extensive driver
	* [SMBus Abstration Repo](https://github.com/gkluoe/micropython-smbus) - use this i2c SMBus layer instead of the i2c.py provided with the Pimoroni BME680 repo
	* [Analog to Digital ADS115 Repo](https://github.com/adafruit/micropython-adafruit-ads1015) - this will be needed if we decide to use a NO2 or O2 sensor.

* Setting up a static dhcp address for the monitor on the router will greatly reduce the network connection latency (from 4-6 seconds to 2) while increasing consistency on runtimes.

## AQ sites worth tracking

* [OpenAQ](https://openaq.org/) - fighting air inequality through open data, open-source tools, and a global, grassroots community.   Georgetown connections?   [Krista Hasenkopf](https://advanced.jhu.edu/about-us/faculty/christa-hasenkopf/) is a leader at OpenAQ as is [Joe Flasher](https://github.com/jflasher). Their funding primarily comes from [here](https://openaq.org/#/about?_k=28cy2c).

* [CityOS](https://cityos-air.readme.io/) - Sarajevo-based initiative that uses the ESP, DHT-11, and PMS-003 sensors - not weather proof - Neopixels for live AQ visualization. 

* [MySense](https://github.com/teusH/MySense) - Python-based repo that apparently offers a framework for attaching myriads of sensors.  Single contributor seeking funding.

* [Nature publishes a good article on air quality monitoring in East Africa](https://www.nature.com/articles/d41586-018-04330-x) - it also raises GeoHealth's work in [Kenya and Tanzania](https://geohealthhub.org/2016/06/30/usc-training-launches-a-new-era-of-air-pollution-health-research-in-eastern-africa/) which is run out of [NIH](https://www.fic.nih.gov/Programs/Pages/environmental-occupational.aspx).

## Code Still To Do

* Port ESP8266 upgrade code in main~.py to ESP32

## Installation

These instructions are provided for Georgetown students who wish to build GUAQ from scratch in the Maker Hub.   These installation steps are a work in progress but have been tested on Linux and Mac OSX systems:

1. Before you install MicroPython - Have you:
	- Confirmed access to Wifi and have obtained the Wifi SSID and password?
	- Located your Adafruit IO Key and Username?
	- Identified how you will power the unit with a USB cable?
	- Located a site suitable for hosting this monitor?
	- Checked that Python Version 2 or Version 3 has been installed on your computer.
	- Downloaded CoolTerm for the Mac or Putty for the PC and configure it to support the ESP32.
		- CoolTerm Configuration: Options->Terminal-"115200", Check "Filter ASCII Escape Sequences" and "Handle BS and DEL Characters" boxes.
	- Chosen a text editor that you're comfortable using to modify Python files.  Sublime Text is a great choice.
	- Bookmarked http://docs.micropython.org/en/latest/esp32/quickref.html. MicroPython is a rich, vibrant development environment.  You should definitely bookmark the following documentation which goes into far more detail than I can cover here.
	

1. With these basics out of the way:

	- Install esptool.py and ampy.py tools on your system by following the instructions in the links below.  Understand how to invoke them from the command line.  
	- Download/Clone this Git repository to a directory of your choice on your computer.
	- Unzip this archive which will create a directory called "air-quality-master".
	- Fetch the required Python library modules listed below from their Git repositories and put these libraries into the current 'air-quality-master' directory.  As a minimum, this must include BME280, BME680, and smbus modules (bme680 and usmbus have library sub-directories)
	- Configure the config-generic.py with the configuration information specific to your site and rename it config.py - these changes will include Wifi credentials and Adafruit IO username and key. Optionally, you can configure the Access Point SSID and password as well.
	- Edit the wake.py file to selectively measure from the attached sensors.  The stub.py can be used when no sensors are available but you want to test the ESP32 and its connectivity to the IOT service.
	- Optionally remove those MicroPython modules that are not required for this monitor - eg. DHT11, analog.py, stub.py, and enviro.py.
	- Use the <span style="font-family:Courier;">utilities/upload</span> script to install Micropython 1.10 on the ESP32 and upload the air quality files.  You will only need to change a single line in this script to identify the port used by your computer to connect to the ESP.  On a macintosh, it's usually  <span style="font-family:Courier;">/dev/tty.usbserial-xxxx</span>.  
	- Run <span style="font-family:Courier;">hwtest.py</span> to confirm that the ESP32 can communicate with the sensors:
	     import hwtest
	- Rename the main\~.py file to main.py so that it runs automatically at boot time.

1. Report any issues to me - fpg13@georgetown.edu
