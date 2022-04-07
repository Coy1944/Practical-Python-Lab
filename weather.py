import requests 

api_key = "665296c092d55883cae9fb30c465822d"
city = "orlando"
url = "https://api.openweathermap.org/data/2.5/weather?="+city+"&appid="+api_key

request = requests.get(url)
json = request.json()
print(json)
