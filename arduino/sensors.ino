#include <Arduino_LPS22HB.h>
#include "Arduino_BMI270_BMM150.h"
#include <Arduino_HS300x.h>

float x, y, z =0;
float temperature = 25;

float pressure = 100;

void setup() {
  Serial.begin(9600);
  Serial1.begin(9600);
  while (!Serial);

  if (!BARO.begin()) {
    Serial1.println("Failed to initialize pressure sensor!");
    while (1);
  }
  if (!IMU.begin()) {
    Serial1.println("Failed to initialize IMU!");
    while (1);
  }
  if (!HS300x.begin()) {
    Serial1.println("Failed to initialize humidity temperature sensor!");
    while (1);
  }

  Serial1.print("Accelerometer sample rate = ");
  Serial1.print(IMU.accelerationSampleRate());
  Serial1.println(" Hz");

  // put your setup code here, to run once:
}

void loop() {
  pressure = BARO.readPressure();
  //Serial1.print("pressure=");
  
  //Serial1.println("kPa");

  //float x, y, z;

  if (IMU.accelerationAvailable()) {
    IMU.readAcceleration(x, y, z);
  }
/*
  if(x > 0.1){
    //x = 0.01*x;
    //degreesX = map(x, 0, 97, 0, 90);
    Serial1.print("Tilting up ");
    Serial1.print(x);
    Serial1.println("  degrees");
  }
  if(x < -0.1){
    x = 0.01*x;
    degreesX = map(x, 0, -100, 0, 90);
    Serial1.print("Tilting down ");
    Serial1.print(x);
    Serial1.println("  degrees");
  }
  if(y > 0.1){
    y = 0.01*y;
    degreesY = map(y, 0, 97, 0, 90);
    Serial1.print("Tilting left ");
    Serial1.print(y);
    Serial1.println("  degrees");
  }
  if(y < -0.1){
    y = 100*y;
    degreesY = map(y, 0, -100, 0, 90);
    Serial1.print("Tilting right ");
    Serial1.print(y);
    Serial1.println("  degrees");
  }*/
  temperature = HS300x.readTemperature();

  Serial1.print(pressure);
  Serial1.print(" , ");

  //Serial1.print("Temperature = ");
  Serial1.print(temperature);
  Serial1.print(" , ");
  //Serial1.println(" °C");

  
  
  //Serial1.println("Gyro data");
  Serial1.print(x);
  Serial1.print(" , ");
  //Serial1.println("°");
  Serial1.print(y);
  Serial1.print(" , ");
  //Serial1.println("°");
  Serial1.print(z);
  Serial1.print(" , ");
  //Serial1.println("°");
  
  float altitude = 44330 * ( 1 - pow(pressure/101.325, 1/5.255) );
  

  // print the sensor value
  //Serial1.print("Altitude according to kPa is = ");
  Serial1.print(altitude);
  //Serial1.println(" m");
  Serial1.println("");
  delay(500);
  Serial.print(altitude);
  Serial1.println("");
  Serial.print(x);
  Serial1.println("");
  Serial.print(y);
  Serial1.println("");
  Serial.print(z);
  Serial1.println("");
  Serial.print(temperature);

  // put your main code here, to run repeatedly:

}