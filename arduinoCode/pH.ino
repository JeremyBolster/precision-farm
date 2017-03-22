
#define Offset 0.00

String readpH() {
  float voltage = analogRead(pH_PIN)*5.0/1024;
  float pHValue = 3.5*voltage+Offset;
//  Serial.print("Voltage:");
//  Serial.print(voltage,2);
  return String("pH value: " + String(pHValue));
//  Serial.print("pH value: ");
//  Serial.println(pHValue,2);
}

