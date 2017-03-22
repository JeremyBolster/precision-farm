String readAirStats() {

  int chk = DHT11.read(AIR_STATS_PIN);

  String conditionCode;
  switch (chk)
  {
    case DHTLIB_OK: 
    conditionCode = "OK"; 
    break;
    case DHTLIB_ERROR_CHECKSUM: 
    conditionCode = "Checksum error"; 
    break;
    case DHTLIB_ERROR_TIMEOUT: 
    conditionCode = "Time out error"; 
    break;
    default: 
    conditionCode = "Unknown error"; 
    break;
  }
  String humidity = String("Humidity (%): " + String((float)DHT11.humidity));
  String temperature = String("Air Temperature (°C): " + String((float)DHT11.temperature));
  return String(humidity + "\n" + temperature);
//  Serial.print("Humidity (%): ");
//  Serial.println((float)DHT11.humidity, 2);
//
//  Serial.print("Air Temperature (°C): ");
//  Serial.println((float)DHT11.temperature, 2);
}


