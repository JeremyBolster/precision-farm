#Food Computer TODO list


##Needs 
* <strike>Solder extra power wires</strike>
* <strike>Make sure all wires are plugged in correctly</strike>
* <strike>Logic in python to control the environment based on the climate recipe</strike>
* <strike>Mount everything on the box</strike>

##By Semester's End
* Averaging filter in python for more accuracy
* Make some sort of wiki (Bookstack)
* Make some sort of UI 
* Create documentation of how to use the software and how to extend it for further use. 

##Stretch
* Give python script parameters for file to run, current day of recipie, etc
* Modularize the sensor 'drivers' to make it easier to use different sensors
* Make it easy to swap sensors
* Send sensor data from python script to influxDB for storage
* Access influxDB from Grafana to view historical and realtime data
* Change current recipie, see current day of recipe in Grafana
* See the camera from Grafana
* Reverse proxy Grafana through apache

##Super-Strech
* Create new recipes through Grafana interface
* Modify existing recipies through Grafana interface
* View historical data for current grow recipie cycle
* View historical data for previous grow recipie executions
* Implement an alerting system to email/text if the pH (or whatever) goes wacky
* edit the python logic parameters from the Grafana interface
* Authentication levels for grafana (anyone should be able to view, only some should be able to edit settings)
* Modify the arduio comms to use CmdMessenger, python to use PyCmdMessenger




