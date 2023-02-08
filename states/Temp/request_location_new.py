import json
import re
from typing import Dict, Optional
# from . import connect_rapid_api
from loader import rapid_api
from logger_config import logger
import requests


# @logger.catch
location_group = 'CITY'
location = 'Вьетнам'
def request_location(location_group: str, location: str) -> Optional[Dict]:

    """
    Принимает на вход строку и возвращает словарь с ID наиболее близких к введённой строке локаций.
    Если возникли проблемы с подключением к API, возвращает сообщение об ошибке.

    :param location_group: группа, в которой ищем локацию
    :type location_group: str
    :param location: локация, указанная пользователем
    :type location: str
    :return: locations_id или None
    :rtype: Dict[str]
    """
    url = "https://hotels4.p.rapidapi.com/locations/v3/search"
    headers = {
        "X-RapidAPI-Key": "06dd932f31msh0a52e2bdec9c858p132b0cjsnd04a260d0e20",
        "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
    }
    req_params = {"q": location, "locale": "ru_RU", "langid": "1033", "siteid": "300000001"}
    response = requests.request("GET", url, headers=headers, params=req_params)
    # print(response)

    if response:
        # resp_json = json.loads(response.text)
        # with open("locations_v3_paris.json", "w") as file:
        #     json.dump(resp_json, file, indent=4)  # записываем файл для проверки и сохранения в БД
        resp_json = json.loads(response.text)
        locations_dict = {}
        for region in resp_json['sr']:
            for key, value in region.items():
                if value == location_group:
                    city_name = region['regionNames'].get('fullName')
                    city_id = region['gaiaId']
                    locations_dict[city_name] = city_id
        print(locations_dict)
request_location(location_group, location)