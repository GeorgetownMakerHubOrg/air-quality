A MicroPython implementation of STIA315.   This version uses:

1. [D1 Mini from Weemos](https://tinyurl.com/yc5p8gho) in lieu of Adafruit's Feather Huzzah
2. D1 Mini Battery Shield
3. [USB connected Solar Shield](https://tinyurl.com/y77dqpdg)
4. [BME280 sensor (Temp, Press, Humid)](https://tinyurl.com/yafl3h9x) in lieu of DHT11 - 

Discuss with Colin:

1. Feather Huzzah issues re: wake from sleep
2. Power usage - 120ma on wake; 1ma on deep sleep
3. Enviros to include battery voltage, runtime, meminfo
4. Global list for maintaining AQ readings - pass the list 
5. Larger battery?
6. Stevenson screen and/or Acurite shield
7. BME680 or some other sensor?  
8. Lengthening the runtime for burn-in
9. Integration with Wunderground

Code Uses the BME280 GitHub Repo:   https://github.com/catdog2/mpy_bme280_esp8266

