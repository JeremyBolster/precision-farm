import PyCmdMessenger


commands = [["water temp",""],
            ["lux","s"],
            ["pH","ii"],
            ["humidity","i"],
            ["air temp","s"],
            ["CO2",""]]

def __init__(self, arduino):
	self.arduino = PyCmdMessenger.ArduinoBoard(arduino)
    self.cmd = PyCmdMessenger.CmdMessenger(self.arduino,commands)

def pollSensors(self):
    arduinoSerialData.write(b'00');
    time.sleep(1) # wait 1 second for the arduino to register
    arduinoSerialData.write(b'00');
    time.sleep(10) # wait 10 seconds for the sensors to collect data
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


	