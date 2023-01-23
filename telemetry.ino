#include <Wire.h>
#include <Arduino_LPS22HB.h>
#include <Arduino_HTS221.h>
#include <Arduino_LSM9DS1.h>
#include <Adafruit_MPL3115A2.h>
#include <TinyGPS++.h>
#include <SoftwareSerial.h>



// Create instances of the sensors
Arduino_LPS22HB lps = Arduino_LPS22HB();
Arduinot_HTS221 hts = Arduino_HTS221();
Arduino_LSM9DS1 lsm = Arduino_LSM9DS1();
Adafruit_MPL3115A2 mpl = Adafruit_MPL3115A2();
TinyGPSPlus gps;
SoftwareSerial ss(2, 3); // RX, TX

void setup() {
  // Start the I2C and software serial
  Wire.begin();
  ss.begin(9600);

  // Initialize the sensors
   if (!BARO.begin()) {
    Serial.println("Failed to initialize pressure sensor!");
    while (1);
   }
   if (!HTS.begin()) {
    Serial.println("Failed to initialize temperature sensor!");
    while (1);
   }
   if (!IMU.begin()) {
    Serial.println("Failed to initialize IMU!");
    while (1);
   }
    if (!mpl.begin()) {
      Serial.println("Could not find a valid MPL3115A2 sensor, check wiring!");
      while (1);
    }
  void loop() {
    // Read the data from the sensors
    float temperature = HTS.readtemperature();
    float x, y, z;
 if (IMU.gyroscopeAvailable()) {
    IMU.readGyroscope(x, y, z);
  }
    float pressure = Baro.readPressure();
    float altitude = Baro.getAltitude();
    while (ss.available() > 0) {
      gps.encode(ss.read());
    }

    // Create the telemetry string
    String telemetry = "P:" + String(pressure, 2) + "Pa"
                       "T:" + String(temperature, 2) + "C"
                       "X:" + String(x, 2) + "Y:" + String(y, 2) + "Z:" + String(z, 2) +
                       "A:" + String(altitude, 2) + "m";

    if (gps.location.isValid()) {
      telemetry += "Lat:" + String(gps.location.lat(), 6) + "Lon:" + String(gps.location.lng(), 6);


      // Print the telemetry
      Serial.println(telemetry);
    }
    
    delay(1000);
    
  }
