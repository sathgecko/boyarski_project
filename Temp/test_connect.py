import requests
from requests.models import Response
from typing import Optional
from logger_config import logger
# from . import connect_rapid_api
from loader import rapid_api



def connect_rapid_api(url: str, header: dict, req_params: dict) -> Optional[Response]:

	response = requests.request("POST", url, json=req_params, headers=header, timeout=10)

	if response.status_code == requests.codes.ok:
		return response
	else:
		raise ConnectionError(f'Возникли проблемы с подключением к API. Код ответа: {response.status_code}')



req_params = {
	"currency": "USD",
	"eapid": 1,
	"locale": "en_US",
	"siteId": 300000001,
	"destination": {"regionId": "6054439"},
	"checkInDate": {
		"day": 10,
		"month": 10,
		"year": 2022
	},
	"checkOutDate": {
		"day": 15,
		"month": 10,
		"year": 2022
	},
	"rooms": [
		{
			"adults": 2,
			"children": [{"age": 5}, {"age": 7}]
		}
	],
	"resultsStartingIndex": 0,
	"resultsSize": 200,
	"sort": "PRICE_LOW_TO_HIGH",
	"filters": {"price": {
			"max": 150,
			"min": 100
		}}
}

response = connect_rapid_api('https://hotels4.p.rapidapi.com/properties/v2/list', rapid_api, req_params)
print(rapid_api)
print(response)