import requests

# this endpoint tells the current location for international space station
endpoint = 'http://api.open-notify.org/iss-now.json'

response = requests.get(endpoint)

data = response.json()
print(data)
