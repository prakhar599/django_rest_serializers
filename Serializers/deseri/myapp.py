import json
import requests

URL= "http://127.0.0.1:8000/deseri/stucreate/"

data = {
    'name' : 'Anni',
    'roll' : 700,
    'city' : 'delhi',
}
json_data = json.dumps(data)
r = requests.post(url= URL , data = json_data)
print(f'Response from API {r.json()}')
