import requests
import json

class NotFound(Exception):
	pass #goes on without defining anything else in the class

class UnexpectedError(Exception):
	pass

def RequestWeather(city):
	#open config.json for APPID key
	with open('config.json') as f:
		json_config = json.loads(f.read())
		app_id = json_config['open_weather']['app_key']
	response = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+ city +'&APPID='+ app_id)
	if response.status_code == 200:
		yo = response.json()
		temp = round(yo['main']['temp'] - 273.15, 2)
		return {
			"city": city, 
			"temp_c": temp, 
			"description": yo['weather'][0]['description']
			}
	elif response.status_code == 404:
		raise NotFound(response.text)
	else:
		raise UnexpectedError(response.text)

def PrintWeather(data):
	try:
		print("temperature in {0}: {1} celsius, {2}".format(data["city"], str(data["temp_c"]), data['description']))
	except:
		print("Bad Argument Error")