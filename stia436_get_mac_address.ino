// STIA 436: Air Quality Innovation
// Georgetown University, Spring 2019
// Get MAC address from Adafruit Feather HUZZAH
// Derived from https://www.arduino.cc/en/Reference/WiFiMACAddress

#include <SPI.h>
#include <ESP8266WiFi.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define WIFI_SSID "GuestNet"
#define WIFI_PASS ""
WiFiClient client;

// Variable to hold MAC address
byte mac_address[6];                     // the MAC address of your Wifi shield

void setup() {
  // start serial monitor connection
  Serial.begin(115200);
  // connect to wifi
  WiFi.begin(WIFI_SSID, WIFI_PASS);
  Serial.println("Connecting to WiFi...");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
  }

  // get MAC address and print
  WiFi.macAddress(mac_address);
  Serial.print("MAC: ");
  Serial.print(mac_address[5],HEX);
  Serial.print(":");
  Serial.print(mac_address[4],HEX);
  Serial.print(":");
  Serial.print(mac_address[3],HEX);
  Serial.print(":");
  Serial.print(mac_address[2],HEX);
  Serial.print(":");
  Serial.print(mac_address[1],HEX);
  Serial.print(":");
  Serial.println(mac_address[0],HEX);
}

// No need for a loop so leave it empty
void loop () {}
