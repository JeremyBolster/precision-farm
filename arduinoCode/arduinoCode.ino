#include "OneWire.h"
#include "dht11.h"

#define WATER_TEMP_PIN 10
#define LUX_PIN A0
#define pH_PIN A1
#define AIR_STATS_PIN 11
#define CO2_DIGITAL_PIN 12
#define CO2_ANALOG_PIN A2

#define AC_1 2
#define AC_2 3
#define AC_3 4
#define AC_4 5

#define DC_1 6
#define DC_2 7
#define DC_3 8
#define DC_4 9

#define POLL_SYMBOL 48

#define         READ_SAMPLE_TIMES            (10) //number of times to poll each sensor (if looping is required)
#define         READ_SAMPLE_INTERVAL         (50) //wait time between sensor polling

dht11 DHT11;

void setup() {
    Serial.begin(9600);
    for(int i=2; i < 10; i++) {
      pinMode(i, OUTPUT);
    }

    pinMode(WATER_TEMP_PIN, INPUT);
    pinMode(LUX_PIN, INPUT);
    pinMode(pH_PIN, INPUT);
    pinMode(CO2_DIGITAL_PIN, INPUT);
    digitalWrite(CO2_DIGITAL_PIN, HIGH);
}

void loop() {
      delay(1000);
      
    if (Serial.available() >= 2) {
      // read the incoming byte:
      byte incomingByte = Serial.read();

      // say what you got:
//      Serial.print("I received: ");
//      Serial.println(incomingByte, DEC);
                
      if(incomingByte == POLL_SYMBOL) {
        Serial.println("---------Begin Sensor Data---------");
        String waterTemp = readWaterTemp();
        String lux = readLux();
        String pH = readpH();
        String airStats = readAirStats();
        String CO2 = readCO2();
        Serial.println(waterTemp);
        Serial.println(lux);
        Serial.println(pH);
        Serial.println(airStats);
        Serial.println(CO2);
        Serial.println("----------End Sensor Data----------");
        Serial.read();  //get rid of the second byte at this point
      }
      if(AC_1 <= incomingByte && incomingByte <= AC_4) {
        digitalWrite(incomingByte, Serial.read());
        Serial.println("turned on AC");
      }
      if(DC_1 <= incomingByte && incomingByte <= DC_4) {
        digitalWrite(incomingByte, Serial.read());
        Serial.println("turned on DC");
      }
      //lets clear the buffer
      while(Serial.available()){
        Serial.read();
      }
    }
}







