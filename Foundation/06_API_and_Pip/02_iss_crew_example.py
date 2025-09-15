import requests

# this endpoint returns data about astronauts currently in space
endpoint = 'http://api.open-notify.org/astros.json'

response = requests.get(endpoint)

print(response.status_code)

data = response.json()
print(data)

with open('astranouts.txt', 'w') as text_file:
    for item in data['people']:
        text_file.write(item['name'] + '\n')  # added new line character, so each name appears on a new line.
