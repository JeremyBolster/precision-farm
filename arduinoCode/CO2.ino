/*******************Demo for MG-811 Gas Sensor Module V1.1*****************************
Author:  Tiequan Shao: tiequan.shao@sandboxelectronics.com
         Peng Wei:     peng.wei@sandboxelectronics.com
         Modified by Leff from DFRobot, leff.wei@dfrobot.com, 2016-4-21, make the algorithm clearer to user
Lisence: Attribution-NonCommercial-ShareAlike 3.0 Unported (CC BY-NC-SA 3.0)

Note:    This piece of source code is supposed to be used as a demostration ONLY. More
         sophisticated calibration is required for industrial field application.

                                                            Sandbox Electronics    2012-05-31
************************************************************************************/

/************************Hardware Related Macros*********|***************************/
#define         DC_GAIN                      (8.5)   //define the DC gain of amplifier

/**********************Application Related Macros**********************************/
//These values differ from sensor to sensor. User should derermine this value.
#define         ZERO_POINT_X                 (2.602) //lg400=2.602, the start point_on X_axis of the curve
#define         ZERO_POINT_VOLTAGE           (0.324) //define the output of the sensor in volts when the concentration of CO2 is 400PPM
#define         MAX_POINT_VOLTAGE            (0.265) //define the output of the sensor in volts when the concentration of CO2 is 10,000PPM
#define         REACTION_VOLTGAE             (0.059) //define the voltage drop of the sensor when move the sensor from air into 1000ppm CO2

/*****************************Globals***********************************************/
float           CO2Curve[3]  =  {ZERO_POINT_X, ZERO_POINT_VOLTAGE, (REACTION_VOLTGAE / (2.602 - 4))};
//Two points are taken from the curve.With these two points, a line is formed which is
//"approximately equivalent" to the original curve. You could use other methods to get more accurate slope

//CO2 Curve format:{ x, y, slope};point1: (lg400=2.602, 0.324), point2: (lg10000=4, 0.265)
//slope = (y1-y2)(i.e.reaction voltage)/ x1-x2 = (0.324-0.265)/(log400 - log10000)

String readCO2() {
  int percentage;
  float volts;

  volts = MGRead(CO2_ANALOG_PIN);
//  volts = analogRead(CO2_ANALOG_PIN) * 5 / 1024;
//  Serial.print( "SEN0159:" );
//  Serial.print(volts);
//  Serial.print( "V           " );

  percentage = MGGetPercentage(volts, CO2Curve);
  String output = "CO2 (ppm): ";
//  Serial.print("CO2 (ppm): ");
  if (percentage == -1) {
    output = String(output + "-1");
//    Serial.println("-1");
  } else {
    output = String(output + String(percentage));
//    Serial.println(percentage);
  }
  return output;
}
/*****************************  MGRead *********************************************
Input:   mg_pin - analog channel
Output:  output of SEN-000007
Remarks: This function reads the output of SEN-000007
************************************************************************************/
float MGRead(int mg_pin) {
  int i;
  float v = 0;

  for (i = 0; i < READ_SAMPLE_TIMES; i++) {
    v += analogRead(mg_pin);
    delay(READ_SAMPLE_INTERVAL);
  }
  v = (v / READ_SAMPLE_TIMES) * 5 / 1024 ;
  return v;
}

/*****************************  MQGetPercentage **********************************
Input:   volts   - SEN-000007 output measured in volts
         pcurve  - pointer to the curve of the target gas
Output:  ppm of the target gas
Remarks: By using the slope and a point of the line. The x(logarithmic value of ppm)
         of the line could be derived if y(MG-811 output) is provided. As it is a
         logarithmic coordinate, power of 10 is used to convert the result to non-logarithmic
         value.
************************************************************************************/
int  MGGetPercentage(float volts, float *pcurve) {
  volts = volts / DC_GAIN;
  if (volts > ZERO_POINT_VOLTAGE || volts < MAX_POINT_VOLTAGE ) {
    return -1;
  } else {
    return pow(10, (volts - pcurve[1]) / pcurve[2] + pcurve[0]);
    volts = 0;
  }
}
