
#include <SPI.h> //for the SD card module
#include <SD.h> // for the SD card

// Sparkfun SD shield: pin 8
const int chipSelect = 4; 

// Create a file to store the data
File myFile;

void setup() {
  //initializing the DHT sensor

  //initializing Serial monitor
  Serial.begin(9600);
  
  // setup for the RTC
    
  // setup for the SD card
  Serial.print("Initializing SD card...");

  if(!SD.begin(chipSelect)) {
    Serial.println("initialization failed!");
    return;
  }
  Serial.println("initialization done.");
    
  //open file
  myFile=SD.open("SYSINFO.txt", FILE_READ);

  // if the file opened ok, write to it:
  if (myFile) {
    Serial.println("File opened ok");
    // print the headings for our data
    myFile.println("Date,Time,Temperature ºC");
  }
  myFile.close();
}

void loggingTime() {
  DateTime now = rtc.now();
  myFile = SD.open("DATA.txt", FILE_WRITE);
  if (myFile) {
    myFile.print(now.year(), DEC);
    myFile.print('/');
    myFile.print(now.month(), DEC);
    myFile.print('/');
    myFile.print(now.day(), DEC);
    myFile.print(',');
    myFile.print(now.hour(), DEC);
    myFile.print(':');
    myFile.print(now.minute(), DEC);
    myFile.print(':');
    myFile.print(now.second(), DEC);
    myFile.print(",");
  }
  Serial.print(now.year(), DEC);
  Serial.print('/');
  Serial.print(now.month(), DEC);
  Serial.print('/');
  Serial.println(now.day(), DEC);
  Serial.print(now.hour(), DEC);
  Serial.print(':');
  Serial.print(now.minute(), DEC);
  Serial.print(':');
  Serial.println(now.second(), DEC);
  myFile.close();
  delay(1000);  
}

void loggingTemperature() {
  // Reading temperature or humidity takes about 250 milliseconds!
  // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
  // Read temperature as Celsius
  float t = dht.readTemperature();
  // Read temperature as Fahrenheit
  //float f = dht.readTemperature(true);
  
  // Check if any reads failed and exit early (to try again).
  if  (isnan(t) /*|| isnan(f)*/) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }
  
  //debugging purposes
  Serial.print("Temperature: "); 
  Serial.print(t);
  Serial.println(" *C");
  //Serial.print(f);
  //Serial.println(" *F\t"); 
  
  myFile = SD.open("DATA.txt", FILE_WRITE);
  if (myFile) {
    Serial.println("open with success");
    myFile.print(t);
    myFile.println(",");
  }
  myFile.close();
}

void loop() {
  loggingTime();
  loggingTemperature();
  delay(5000);
}
void setup()
{
  Serial.begin(115200);
  //Serial1.begin(115200);
  Serial1.begin(115200);
  
}

void loop()
{
  Serial1.print("HelloWorld\n");
  Serial2.flush();
  //while(Serial2.read());
  if(Serial.available())
  {
    while(Serial.available()>0)
    {
      char inByte = Serial.read();
      Serial.print(inByte);
    }
    Serial.print('\n');
    Serial.flush();
  }
  delayMicroseconds(1);}