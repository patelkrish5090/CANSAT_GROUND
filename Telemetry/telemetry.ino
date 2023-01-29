#include <Wire.h>
#include <Arduino_LPS22HB.h>
#include <Arduino_HTS221.h>
#include <Arduino_LSM9DS1.h>
#include <Adafruit_MPL3115A2.h>
#include <TinyGPS++.h>
#include <SoftwareSerial.h>



// Create instances of the sensors
Arduino_LPS22HB lps = Arduino_LPS22HB();
Arduino_HTS221 hts = Arduino_HTS221();
Arduino_LSM9DS1 imu = Arduino_LSM9DS1();
Adafruit_MPL3115A2 mpl = Adafruit_MPL3115A2();
TinyGPSPlus gps;
// UART mySerial(digitalPinToPinName(RX of Xbee), digitalPinToPinName(TX of Xbee), NC, NC);
UART mySerial(digitalPinToPinName(2), digitalPinToPinName(3), NC, NC);

void setup() {
  // Start the I2C and UART Myserial
  Wire.begin();
  mySerial.begin(9600);

  // Initialize the sensors
  Serial.begin(9600);
  while (!Serial);
  
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
    float temperature = HTS.readTemperature();
    float X, Y, Z;
 if (IMU.gyroscopeAvailable()) {
    IMU.readGyroscope(X, Y, Z);
  }
    float pressure = Baro.readPressure();
    float altitude = Baro.getAltitude();
    while (mySerial.available() > 0) {
      gps.encode =mySerial.read());
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
