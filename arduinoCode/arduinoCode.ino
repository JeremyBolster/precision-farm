#include "OneWire.h"
#include "dht11.h"
#include "CmdMessenger.h"

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

#define         READ_SAMPLE_TIMES            (10) //number of times to poll each sensor (if looping is required)
#define         READ_SAMPLE_INTERVAL         (50) //wait time between sensor polling

dht11 DHT11;
CmdMessenger c = CmdMessenger(Serial,',',';','/');

void setup() {
    Serial.begin(9600);
    for(int i=2; i < 10; i++) {
      pinMode(i, OUTPUT);
    }
    digitalWrite(AC_1, HIGH);
    digitalWrite(AC_2, HIGH);
    digitalWrite(AC_3, HIGH);
    digitalWrite(AC_4, HIGH);

    pinMode(WATER_TEMP_PIN, INPUT);
    pinMode(LUX_PIN, INPUT);
    pinMode(pH_PIN, INPUT);
    pinMode(CO2_DIGITAL_PIN, INPUT);
    digitalWrite(CO2_DIGITAL_PIN, HIGH);
    attach_callbacks();  
}

void loop() {
    c.feedinSerialData();
}

/* Define available CmdMessenger commands */
enum {
    sensor_poll,
    sensor_data,
    toggle_device,
    error,
};

void on_sensor_poll(void){
  String waterTemp = readWaterTemp();
  String lux = readLux();
  String pH = readpH();
  String airStats = readAirStats();
  String CO2 = readCO2();
  c.sendCmdStart(sensor_data);
  c.sendCmdArg(waterTemp);
  c.sendCmdArg(lux);
  c.sendCmdArg(pH);
  c.sendCmdArg(airStats);
  c.sendCmdArg(CO2);
  c.sendCmdEnd();
}

void on_toggle_device(void){
  int pinNumber = c.readBinArg<int>();
  bool pinSetting = c.readBinArg<bool>();
  digitalWrite(pinNumber, pinSetting);
}

/* callback */
void on_unknown_command(void){
    c.sendCmd(error,"Command without callback.");
}

/* Attach callbacks for CmdMessenger commands */
void attach_callbacks(void) { 
    c.attach(sensor_poll,on_sensor_poll);
    c.attach(toggle_device,on_toggle_device);
    c.attach(on_unknown_command);
}






