import WeatherFromWeb

city = input("Enter a city: ")

try:
	weather_data = WeatherFromWeb.RequestWeather(city)
	WeatherFromWeb.PrintWeather(weather_data)
except WeatherFromWeb.NotFound as e:
	print("City was not found!")
	print(e.args[0])
except WeatherFromWeb.UnexpectedError as e:
	print('An unexpected error occured!')
	print(e.args[0])

print("")
# input()
