# STIA 436 - Air Quality Innovation

## Improvements on the [STIA315](https://github.com/colinmccormick/Georgetown_STIA315_AQ_monitor) course.   

These include:

1. Code written in Micropython
1. Integrated battery shield and Expressif ESP32 WROOM-32 circuitry on single board (Lolin D32)
1. Stevenson case to improve air flow
1. Crisp wiring that leverages the I2C bus
1. Full deep-sleep & wake cycling
1. Significant cost reduction (66% reduction)
1. Lithium Ion Battery with 20% greater mAh at 87% cost savings over LiPo
1. Four (4) 16bit Analog Channels for ADC sensors
1. Voltage monitoring on a ADC channel

## Prototype Components

The prototype has the following components:

1. [LOLIN D32 ESP32 Board ](https://wiki.wemos.cc/products:d32:d32)
1. [Stevenson enclosure from Thingiverse](http://www.thingiverse.com/thing:2282869) - courtesy [Open Green Energy](https://www.opengreenenergy.com/)
1. I2C-based Sensors:
	1. [BME280 sensor (Temperature, Pressure, Humidity)](https://tinyurl.com/yafl3h9x)
	1. [BME680 sensor (Temperature, Pressure, Humidity, and Carbon-based Gas Particles)](https://www.bosch-sensortec.com/bst/products/all_products/bme680)
1. [USB connected Solar Panel](https://tinyurl.com/yad7xpcu)
1. [Optional 3000mAh 18650 Lithium Ion Battery](https://www.ebay.com/itm/202512035904)

The available I2C devices are set to the following addresses:

* 118 (0x76) - BME280 Sensor
* 119 (0x77) - BME680 Sensor

## Open Actions/Areas of Investigation & Improvement:

1. Continue to evaluate power usage using the DC Power Supply in the Hub. Are sensors unnecessarily draining the battery?  Currently, the unit draws 75 mA running and 2 mA in deep sleep - much of the draw during sleep is from the sensors.  At a 1 minute sampling, we can go about 10 days (without using the 680 or 30105) 
<<<<<<< HEAD
1. Better understanding of the accuracy and target purpose of the Bosch BME680 Sensors.  More and more articles are appearing on this subject of Consumer Grade Air Quality Monitoring such as [this](https://molekule.com/blog/consumer-grade-air-quality-sensors-are-they-good-enough/).  [Volatile Organic Compounds](https://toxtown.nlm.nih.gov/chemicals-and-contaminants/volatile-organic-compounds-vocs) are nasty!  Let's also look at [laser-based PM2.5 sensors with fans](https://aqicn.org/sensor/pms5003-7003/).  A [decent listing of AQ sensors](https://aqicn.org/sensor/) is, of course, in China.   [Super interesting paper](https://uwspace.uwaterloo.ca/bitstream/handle/10012/12776/Tan_Ben.pdf?sequence=5) on the Plantower sensors. We're on the right track with our sensors - check [this](https://seetheair.wordpress.com/2019/01/15/review-purpleair-ii/) out.  A [DIY site](https://www.byteyourlife.com/en/household-tools/particulate-matter-sensor-controller-project-luftdaten-info/7204) where you can register your device.
1. This repo is migrating to the ESP32 MCU.   There are minor implementation differences that we'll need to manage (eg. sleep-ESP8266.py vs. sleep.py)
1. Better understanding of the accuracy and target purpose of the PMS-A003 and Bosch BME680 Sensors.  More work is needed here but here's [a good starting point](https://hackaday.io/project/18518-iteration-8/log/55721-a-first-attempt-at-figuring-out-the-max30105-air-particle-sensor).  More and more articles are appearing on this subject of Consumer Grade Air Quality Monitoring such as [this](https://molekule.com/blog/consumer-grade-air-quality-sensors-are-they-good-enough/).  [Volatile Organic Compounds](https://toxtown.nlm.nih.gov/chemicals-and-contaminants/volatile-organic-compounds-vocs) are nasty!  Let's also look at [laser-based PM2.5 sensors with fans](https://aqicn.org/sensor/pms5003-7003/).  A [decent listing of AQ sensors](https://aqicn.org/sensor/) is, of course, in China.   [Super interesting paper](https://uwspace.uwaterloo.ca/bitstream/handle/10012/12776/Tan_Ben.pdf?sequence=5) on the Plantower sensors. We're on the right track with our sensors - check [this](https://seetheair.wordpress.com/2019/01/15/review-purpleair-ii/) out.  A [DIY site](https://www.byteyourlife.com/en/household-tools/particulate-matter-sensor-controller-project-luftdaten-info/7204) where you can register your device.
1. Integration with other IoT sites - ThingSpeak, Wunderground.
1. Let's track low power options like [nanoPower](http://nanopower.no/#p) which uses the nrf chipset from Norway.

## Possible Improvements:

1. If Lithium battery hits a certain threshold, enter deep sleep to prevent total depletion.
1. Set alerts using IFTTT webhooks to alert when battery hits a threshold.
1. The BME280 draws power from the 3.3v even during ESP deep sleep. Can we invoke deep sleep on sensors too prior to shutting down the ESP?

## Notes

* [So much open source technology packed in a small space!](./D1-STIA436.jpg)

* You will need the following tools with this project:

	1. [esptool.py](https://github.com/espressif/esptool) - for flashing MicroPython on the D1 Lolin/Wemos Pro
	1. [ampy](https://github.com/pycampers/ampy) - for uploading/downloading/list files on the D1.
	1. [MicroPython](https://github.com/micropython) - if you're up for building from source!
	1. [WebREPL files](https://github.com/micropython/webrepl) to access the ESP wirelessly

* Two test units are in prototype: [School](https://io.adafruit.com/fpgirard/dashboards/school) and [Bethesda]().

* This code base leverages several other important MicroPython repositories including but not limited to:
	* [BME280 Repo](https://github.com/catdog2/mpy_bme280_esp8266) - 
	* [Pimoroni BME680 Repo](https://github.com/pimoroni/bme680-python) - extensive driver
	* [SMBus Abstration Repo](https://github.com/gkluoe/micropython-smbus) - use this i2c SMBus layer instead of the i2c.py provided with the Pimoroni BME680 repo

## AQ sites worth tracking

* [CityOS](https://cityos-air.readme.io/) - Sarajevo-based initiative that uses the ESP, DHT-11, and PMS-003 sensors - not weather proof - Neopixels for live AQ visualization. 

* [MySense](https://github.com/teusH/MySense) - Python-based repo that apparently offers a framework for attaching myriads of sensors.  Single contributor seeking funding.

* [OpenAQ](https://openaq.org/) - fighting air inequality through open data, open-source tools, and a global, grassroots community.   Georgetown connections?   [Krista Hasenkopf](https://advanced.jhu.edu/about-us/faculty/christa-hasenkopf/) is a leader at OpenAQ as is [Joe Flasher](https://github.com/jflasher). Their funding primarily comes from [here](https://openaq.org/#/about?_k=28cy2c).



