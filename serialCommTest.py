import serial 
import time
arduinoSerialData = serial.Serial('/dev/tty.usbmodem1411',9600)
# arduinoSerialData.write(bytes(chr(0x06),'ASCII'))
while True:
	if(arduinoSerialData.inWaiting()):
		myData = arduinoSerialData.readline().decode('utf-8')
		print(myData)
	else:
		arduinoSerialData.write(bytes(chr(0x06),'ASCII'))
		arduinoSerialData.write(bytes(chr(0x01),'ASCII'))
		time.sleep(2)
