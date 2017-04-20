import PyCmdMessenger


sensors = [["water temp",""],
            ["lux","s"],
            ["pH","ii"],
            ["humidity","i"],
            ["air temp","s"],
            ["CO2",""]]

devices = {"Heater" : "AC1", 
			"Lights" : "AC2",
			"Humidifier" : "AC3",

			"FAN1" : "DC1",
			"FAN2" : "DC2"}
'''
Heater = AC1
Lights = AC2
Humidifier = AC3


FAN1 = DC1
FAN2 = DC2
'''
class ArduinoMessenger:
	
	def __init__(self, arduino):
		self.arduino = PyCmdMessenger.ArduinoBoard(arduino)
		self.cmd = PyCmdMessenger.CmdMessenger(self.arduino,commands)

	def toggleDevice(self, device, value):
		cmd.send(devices[device] +" "+ value)

	def pollSensors(self):

	    data = {} 
	    for sensor in sensors:
	    	cmd.send(sensor[0])
	    	data[sensor[0]] = cmd.receive()[0][0]

	    return data


	