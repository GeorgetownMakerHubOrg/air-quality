# STIA 436 STIA 436 - Air Quality Innovation

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

## This prototype includes the following components:

1. [Wemos D1 Mini Pro](***)
1. [Stevenson enclosure from Thingiverse](http://www.thingiverse.com/thing:2282869) - courtesy [Open Green Energy](https://www.opengreenenergy.com/)
1. 4 I2C-based Sensors:
	1. [BME280 sensor (Temperature, Pressure, Humidity)](https://tinyurl.com/yafl3h9x)
	1. [BME680 sensor (Temperature, Pressure, Humidity, and Carbon-based Gas Particles)]https://www.bosch-sensortec.com/bst/products/all_products/bme680)
	1. [MAX30105 IR Sensor (PM2.5 Sensor)](https://www.maximintegrated.com/en/products/sensors/MAX30105.html)
	1. [ADS1115 ADC Channel Board](https://www.adafruit.com/product/1085)
1. [USB connected Solar Shield](https://tinyurl.com/yad7xpcu)
1. [2500mAh LiPo Battery](https://www.adafruit.com/product/328)

## Open Actions/Areas of Investigation & Improvement:

1. Continue to evaluate power usage using the DC Power Supply in the Hub. Are sensors unnecessarily draining the battery?   
1. Better understanding of the accuracy and target purpose of the MAX30105 and Bosch BME680 Sensors.  More work is needed here but here's [a good starting point.](https://hackaday.io/project/18518-iteration-8/log/55721-a-first-attempt-at-figuring-out-the-max30105-air-particle-sensor)
1. Integration with other IoT sites - ThingSpeak, Wunderground.

## Possible Improvements:

1. If LiPo battery hits a certain threshold, enter deep sleep to prevent total depletion.
1. Set alerts using IFTTT webhooks to alert when battery hits a threshold.
1. The BME280 draws power from the 3.3v even during ESP deep sleep. Can we invoke deep sleep on sensors too prior to shutting down the ESP?

## Notes
[So much open source technology packed in a small space!](./D1-STIA436.jpg) 

* 2 Test Units are in prototype: [School](https://io.adafruit.com/fpgirard/dashboards/school) and [Bethesda]().
* This code base leverages several other important MicroPython repositories including but not limited to:
	* BME280 GitHub Repo](https://github.com/catdog2/mpy_bme280_esp8266)
	* [BME680 GitHub Repo]()
	* [MAX30105 GitHub Repo]()
	* [ADS1115 GitHub Repo](https://github.com/adafruit/micropython-adafruit-ads1015)

