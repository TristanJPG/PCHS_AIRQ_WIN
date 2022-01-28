import requests
from pprint import pprint
from sender import Sender
# id = 90171 #installation ID
# id = 7276 #sensor ID

# url = "https://airapi.airly.eu/v2/installations/sensor?sensorId=7276"
# url2 = " https://airapi.airly.eu/v2/installations/90171"
url3 = "https://airapi.airly.eu/v2/measurements/installation"
headers = {
    "apikey": "YxcTEp46sDPfOazSy7wuRRaMF3hjUE1r"
}
params = {
    "installationId": 90171
}



r = requests.get(url=url3, headers=headers, params=params)
data = r.json()
values = data['current']['values']
title = []
matter = []

for value in values:
    # pprint(f"{value['name']} " + f"{value['value']}")
    title.append(value['name'])
    matter.append(value['value'])
    k = dict(zip(title, matter))

s = Sender(title, matter)

