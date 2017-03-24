import serial 
import time
arduinoSerialData = serial.Serial('/dev/tty.usbmodem1411',9600)
while True:
	if(arduinoSerialData.inWaiting()):
		myData = arduinoSerialData.readline().decode('utf-8')
		print(myData)
	else:
		arduinoSerialData.write(b'00')
		time.sleep(2)
