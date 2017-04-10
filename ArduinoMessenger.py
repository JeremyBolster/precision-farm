import PyCmdMessenger

sensors = ["water_temp","lux","pH","humidity","air_temp","CO2"]

devices = {"heater" : "AC1", 
			"lights" : "AC2",
			"humidifier" : "AC3",

			"fan1" : "DC1",
			"fan2" : "DC2"}

			#define AC_1 2
#define AC_2 3
#define AC_3 4
#define AC_4 5

#define DC_1 6
#define DC_2 7
#define DC_3 8
#define DC_4 9
devices_pins ={"AC1" : 2, "AC2" : 3, "AC3" : 4, "AC4" : 5,
				"DC1" : 6, "DC2" : 7, "DC3" : 8, "DC4" : 9}

commands = [["sensor_poll",""],
			["sensor_data", "sssss"],
			["toggle_device","i"]]

class ArduinoMessenger:

	def __init__(self, arduino):
		self.arduino = PyCmdMessenger.ArduinoBoard(arduino)
		self.cmd = PyCmdMessenger.CmdMessenger(self.arduino,commands) 
			#TODO need to add the devices to the commands

	def toggleDevice(self, device, value):
		cmd.send(devices[device] +" "+ value)
		#THIS IS WRONG should send multiple arguments

	def pollSensors(self):

	    data = {} 
	    for sensor in sensors:
	    	cmd.send(sensor[0])
	    	data[sensor[0]] = cmd.receive()[0][0] #TODO this is just a string

	    	# if(lines[0].find('Water Temp') != -1):
      #       data['waterTemp'] = float(lines[-1])

	    return data


	