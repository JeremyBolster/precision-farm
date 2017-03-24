import serial 
import time
import json

pollSensorsCode = b'00'
pollInterval = 5 #time between sensor and reaction intervals in seconds
numSensors = 6


'''config for communication'''
arduinoSerialData = serial.Serial('/dev/tty.usbmodem1411',9600)
# arduinoSerialData.flushOutput()
# arduinoSerialData.flushInput()

'''Current Time'''
startTime = time.time()


'''Read climate recipe'''
#TODO parameterize the file we use.

def executeParameters(pattern):
    patternExecutionTime = pattern['hours'] * 60 * 60 * 1000 # hours -> minutes -> seconds -> ms
    while (startTime + patternExecutionTime) > time.time():
        currentTime = time.time()
        data = pollSensors()
        print(data)

        if(data['lux'] < pattern['light_illuminance']): #this may require toggleing
            #TODO turn on lights
            time.sleep(1) #debug remove

        if(data['airTemp'] < pattern['air_temperature']):
            #TODO turn on the heater
            #TODO implement tolerence range values (So it doesn't click on and off quickly)
            #TODO add a warning of somekind if it goes over the temperature + tolerance level
            time.sleep(1) #debug remove

        # if(data['humidity'] < pattern['humidity']):
        #     #TODO turn on the sensor
        #     #TODO implement tolerence range values
        #     #TODO check if this is the correct name in patterns
        #     time.sleep(1) #debug remove

        while currentTime + pollInterval > time.time(): #lets only poll the sensors every once in a while
            time.sleep(1)



def pollSensors():
    arduinoSerialData.write(b'00');
    time.sleep(5) # wait 5 seconds for the sensors to collect data
    arduinoSerialData.write(b'00');
    time.sleep(5) # wait 5 seconds for the sensors to collect data
    data = {} 
    while arduinoSerialData.inWaiting():
        myData = arduinoSerialData.readline().decode('utf-8')
        # print(myData) #TODO debug
        lines = myData.split(':')
        #This is gross 🤢 😓
        if(lines[0].find('Water Temp') != -1):
            data['waterTemp'] = float(lines[-1])
        elif(lines[0].find('lux') != -1):
            data['lux'] = float(lines[-1])
        elif(lines[0].find('pH') != -1):
            data['pH'] = float(lines[-1])
        elif(lines[0].find('Humidity') != -1):
            data['humidity'] = float(lines[-1])
        elif(lines[0].find('Air Temp') != -1):
            data['airTemp'] = float(lines[-1])  
        elif(lines[0].find('CO2') != -1):
            data['CO2'] = float(lines[-1])

        if len(data) == numSensors:
            return data

with open('general_greens.json') as data_file:    
    data = json.load(data_file)
    print()
    print('The current climate recipe is: '+data['_id'])
    print()
    # operations is the control data for the farm; we only really care about this
    # it can have multiple stages we can iterate through them from the len(data['operations'])
    operations = data['operations']
    for currentOperation in range(0, len(operations)):
        currentPattern = operations[currentOperation]
        patternDays = currentPattern['cycles']
        day = currentPattern['day']
        night = currentPattern['night']

        #TODO should we be in night or day and at which hour to start????

        executeParameters(day)
        executeParameters(night)
        for i in range(0, patternDays):
            print('days of cycle ' + str(currentOperation) + ' have these parameters: ' + str(day))
            print('nights of cycle ' + str(currentOperation) + ' have these parameters: ' + str(night))


'''
---------Begin Sensor Data---------

Water temp (°C): 24.56

lux: 0

pH value: 2.87

Humidity (%): 33.00

Air Temperature (°C): 24.00

CO2 (ppm): -1

----------End Sensor Data----------
'''

'''test 2 -- communication and control --'''
# while True:
#   if(arduinoSerialData.inWaiting()):
#       myData = arduinoSerialData.readline().decode('utf-8')
#       print(myData)
#       lines = myData.split(':')
#       for i in range(0,len(lines)):
#           try:
#               print(float(lines[i]))
#           except ValueError:
#               continue
#   else:
#       arduinoSerialData.write(bytes(input(),'ASCII'))