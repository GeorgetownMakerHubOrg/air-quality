# STIA 436 - Air Quality Innovation

## Improvements on the [STIA315](https://github.com/colinmccormick/Georgetown_STIA315_AQ_monitor) course.   

These include:

1. Code written in Micropython
1. Integrated battery shield and ESP8226 circuitry on single board (Lolin D1 Pro)
1. Voltage monitoring on A0 Pin
1. Stevenson case to improve air flow
1. Crisp wiring that leverages the I2C bus
1. Full deep-sleep & wake cycling
1. Four (4) 16bit Analog Channels for ADC sensors
1. Significant cost reduction (50% reduction)
1. Lithium Ion Battery with 20% greater mAh at 87% cost savings over LiPo

## Prototype Components

The prototype has the following components:

1. [Wemos D1 Mini Pro](***)
1. [Stevenson enclosure from Thingiverse](http://www.thingiverse.com/thing:2282869) - courtesy [Open Green Energy](https://www.opengreenenergy.com/)
1. 4 I2C-based Sensors:
	1. [BME280 sensor (Temperature, Pressure, Humidity)](https://tinyurl.com/yafl3h9x)
	1. [BME680 sensor (Temperature, Pressure, Humidity, and Carbon-based Gas Particles)](https://www.bosch-sensortec.com/bst/products/all_products/bme680)
	1. [MAX30105 IR Sensor (PM2.5 Sensor)](https://www.maximintegrated.com/en/products/sensors/MAX30105.html)
	1. [ADS1115 ADC Channel Board](https://www.adafruit.com/product/1085)
1. [USB connected Solar Shield](https://tinyurl.com/yad7xpcu)
1. [2500mAh LiPo Battery](https://www.adafruit.com/product/328)

The I2C devices are set to the following addresses:

* 72 (0x48) - ADS1115 Analog-To-Digital Converter
* 87 (0x57) - MAX30105 IR Sensor
* 118 (0x76) - BME280 Sensor
* 119 (0x77) - BME680 Sensor

## Open Actions/Areas of Investigation & Improvement:

1. Continue to evaluate power usage using the DC Power Supply in the Hub. Are sensors unnecessarily draining the battery?  Currently, the unit draws 75 mA running and 2 mA in deep sleep - much of the draw during sleep is from the sensors.  At a 1 minute sampling, we can go about 10 days (without using the 680 or 30105) 
1. Better understanding of the accuracy and target purpose of the MAX30105 and Bosch BME680 Sensors.  More work is needed here but here's [a good starting point.](https://hackaday.io/project/18518-iteration-8/log/55721-a-first-attempt-at-figuring-out-the-max30105-air-particle-sensor)
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

* Two Test Units are in prototype: [School](https://io.adafruit.com/fpgirard/dashboards/school) and [Bethesda]().

* This code base leverages several other important MicroPython repositories including but not limited to:
	* [BME280 GitHub Repo](https://github.com/catdog2/mpy_bme280_esp8266)
	* [BME680 GitHub Repo]()
	* [MAX30105 GitHub Repo]()
	* [ADS1115 GitHub Repo](https://github.com/adafruit/micropython-adafruit-ads1015)

