void setup()
{
  Serial.begin(115200);
  //Serial1.begin(115200);
  Serial1.begin(115200);
  
}

void loop()
{
  Serial1.print(F("HelloWorld\n"));
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