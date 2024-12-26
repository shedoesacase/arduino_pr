#include <Temperature_LM75_Derived.h>
#include <DHT22.h>

Generic_LM75 temperature;
DHT22 dht22(3); 

void setup() {  
  Serial.begin(9600);
  Wire.begin();
}

void loop() {
  
  Serial.print(temperature.readTemperatureC());
  Serial.print(" ");
  Serial.println(dht22.getHumidity());
  delay(500);
}