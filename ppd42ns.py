visit: https://github.com/lvidarte/esp8266

/*
Grove - Dust Sensor Demo v1.0
 Interface to Shinyei Model PPD42NS Particle Sensor
 Program by Christopher Nafis 
 Written April 2012
 
 http://www.seeedstudio.com/depot/grove-dust-sensor-p-1050.html
 http://www.sca-shinyei.com/pdf/PPD42NS.pdf
 
 JST Pin 1 (Black Wire)  =&gt; //Arduino GND
 JST Pin 3 (Red wire)    =&gt; //Arduino 5VDC
 JST Pin 4 (Yellow wire) =&gt; //Arduino Digital Pin 8
 */
 
int pin = 8;
unsigned long duration;
unsigned long starttime;
unsigned long sampletime_ms = 2000;//sampe 30s&nbsp;;
unsigned long lowpulseoccupancy = 0;
float ratio = 0;
float concentration = 0;
 
void setup() {
  Serial.begin(9600);
  pinMode(8,INPUT);
  starttime = millis();//get the current time;
}
 
void loop() {
  duration = pulseIn(pin, LOW);
  lowpulseoccupancy = lowpulseoccupancy+duration;
 
  if ((millis()-starttime) >= sampletime_ms)//if the sampel time = = 30s
  {
    ratio = lowpulseoccupancy/(sampletime_ms*10.0);  // Integer percentage 0=&gt;100
    concentration = 1.1*pow(ratio,3)-3.8*pow(ratio,2)+520*ratio+0.62; // using spec sheet curve
    Serial.print("concentration = ");
    Serial.print(concentration);
    Serial.println(" pcs/0.01cf");
    Serial.println("\n");
    lowpulseoccupancy = 0;
    starttime = millis();
  }
}


Colin's Code: 

void loop() {
  // Check for button A push to pause; resume with button C
  if ( !digitalRead(BUTTON_A) ) {         
    display_text("PAUSED...\nPress C to resume.");
    while ( digitalRead(BUTTON_C) ) { delay(500); } // wait for button C
    display_text("Resuming...\nTTM: "+String(sampleTime/60/1000)+" mins");
    totalStopwatch = 0;     // reset after pause
    startTime = millis();   // reset after pause
  }


  // Monitor pulse length from PPD42NS
  stopwatchDuration = pulseIn(PPDPIN, LOW);   // duration of LOW pulse (microseconds)
  totalStopwatch = totalStopwatch + stopwatchDuration;
  if ((millis() - startTime) >= sampleTime) { // wait until we've hit cycle time
    // Calculate PM2.5 concentration
    ratio = totalStopwatch / (sampleTime * 10.0); // percentage (0 to 100)
    concentration = 1.1 * pow(ratio, 3) - 3.8 * pow(ratio, 2) + 520 * ratio + 0.62; // from manual
    if (concentration > maxConcentration) {   // clip concentration above maximum value
      concentration = maxConcentration;
    }

Ultrasonic Code:

"""Micropython module for HC-SR04 ultrasonic ranging module."""
from machine import Pin, time_pulse_us
from time import sleep_us


class Ultrasonic:
    """HC-SR04 ultrasonic ranging module class."""

    def __init__(self, trig_Pin, echo_Pin):
        """Initialize Input(echo) and Output(trig) Pins."""
        self._trig = trig_Pin
        self._echo = echo_Pin
        self._trig.init(Pin.OUT)
        self._echo.init(Pin.IN)
        self._sound_speed = 340  # m/s

    def _pulse(self):
        """Trigger ultrasonic module with 10us pulse."""
        self._trig.high()
        sleep_us(10)
        self._trig.low()

    def distance(self):
        """Measure pulse length and return calculated distance [m]."""
        self._pulse()
        pulse_width_s = time_pulse_us(self._echo, Pin.high) / 1000000
        dist_m = (pulse_width_s / 2) * self._sound_speed
        return dist_m

    def calibration(self, known_dist_m):
        """Calibrate speed of sound."""
        self._sound_speed = known_dist_m / self.distance() * self._sound_speed
        print("Speed of sound was successfully calibrated! \n" +
              "Current value: " + str(self._sound_speed) + " m/s")

