import serial 
import time
import json

'''config for communication'''
arduinoSerialData = serial.Serial('/dev/tty.usbmodem1411',9600)
arduinoSerialData.flushOutput()
arduinoSerialData.flushInput()

'''test 1 -- communication'''
# arduinoSerialData.write(int(0).to_bytes(1, byteorder='little')) #byte order does not matter for one byte
# while 1:
#   arduinoSerialData.write(int(0).to_bytes(1, byteorder='little')) #byte order does not matter for one byte
#   time.sleep(1)
#   if(arduinoSerialData.inWaiting()):
#       myData = arduinoSerialData.readline()
#       print(myData.decode('utf-8'))

'''test 2 -- communication and control --'''
while True:
  if(arduinoSerialData.inWaiting()):
      myData = arduinoSerialData.readline().decode('utf-8')
      print(myData)
      lines = myData.split(':')
      # for i in range(0,len(lines)):
      #     try:
      #         print(float(lines[i]))
      #     except ValueError:
      #         continue
  else:
      arduinoSerialData.write(bytes(input(),'ASCII'))

'''test 3 -- json ;parsing of input --'''
'''
JSON    Python
object  dict
array   list
string  str
number (int)    int
number (real)   float
true    True
false   False
null    None
'''

# with open('general_greens.json') as data_file:    
#     data = json.load(data_file)
#     print('name: '+data['_id'])
#     print()
#     # operations is the control data for the farm
#     # it can have multiple stages we can iterate through them from the len(data['operations'])
#     operations = data['operations']
#     first_pattern = operations[0]
#     print('cycle one\'s length is: ' + str(first_pattern['cycles']))
#     print()
#     print('days of cycle one have these parameters: ' + str(first_pattern['day']))
#     print()
#     print('nights of cycle one have these parameters: ' + str(first_pattern['night']))












