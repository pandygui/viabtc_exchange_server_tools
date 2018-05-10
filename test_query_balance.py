
#import api.api_exchange.py as ex
from api import api_exchange as ex
import requests, json

ip_exchange = "http://127.0.0.1:18080/"
headers = {'content-type': 'application/json'}

response = requests.post(ip_exchange, data=json.dumps(ex.balance.query(1)), headers=headers)
print(json.loads(response.text))
