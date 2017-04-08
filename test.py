import serial 
import time
import json
from subprocess import call
import datetime
import glob



pollSensorsCode = b'00'
pollInterval = 5 #time between sensor and reaction intervals in seconds
numSensors = 6


'''config for communication'''
arduinoSerialData = serial.Serial(glob.glob("/dev/tty.usbmodem*")[0],9600) 
#TODO this is broken if we want multiple farms on one raspberry pi
#also broken if an arduino is not connected

'''Current Time'''
startTime = time.time()

def executeParameters(pattern):

    patternExecutionTime = pattern['hours'] * 60 * 60 * 1000 # hours -> minutes -> seconds -> ms
    while (startTime + patternExecutionTime) > time.time():

        imageFileName = datetime.datetime.now().strftime("%H:%M:%S:%m:%d:%Y") + '.jpeg'
        call(["fswebcam", "-r 1280x720", imageFileName])

        currentTime = time.time()
        data = pollSensors(arduinoSerialData)
        print(data)
        try:
            if(data['lux'] < pattern['light_illuminance']): #this may require toggleing
                #TODO turn on lights
                pass
        except KeyError:
            pass

        try:
            if(data['airTemp'] < pattern['air_temperature']):
           #      #TODO turn on the heater
           #      #TODO implement tolerence range values (So it doesn't click on and off quickly)
           #      #TODO add a warning of somekind if it goes over the temperature + tolerance level
                pass
        except KeyError:
            pass

        try:
            if(data['humidity'] < pattern['humidity']):
        #     #TODO turn on the sensor
        #     #TODO implement tolerence range values
        #     #TODO check if this is the correct name in patterns
                pass
        except KeyError:
            pass

        while currentTime + pollInterval > time.time(): #lets only poll the sensors every once in a while
            time.sleep(1)


'''Read climate recipe'''
#TODO parameterize the file we use.
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