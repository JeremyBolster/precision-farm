String readLux() {
  return String("lux: " + String(analogRead(LUX_PIN)));
//  Serial.print("lux: ");
//  Serial.println(analogRead(LUX_PIN));
}
