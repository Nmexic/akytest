import requests
url = "https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400"
response = requests.get(url)
data = response.json()
print(data)