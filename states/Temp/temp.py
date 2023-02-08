print(pattern) == (?<=\"CITY_GROUP\",).+?[\]]
print(search_pattern) == <re.Match object; span=(179, 2550), match='"entities":[{"geoId":"6054439","destinationId":"1>
locations_dict = {'Нхатранг, Кханьхоа (провинция), Вьетнам': '6054439', 'ОстровФукуок, Кьензянг (провинция), Вьетнам': '6141655', 'Phan Thiet, Биньтхуан, Вьетнам': '6054401', 'Хошимин, Вьетнам': '3140'}

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

# with open("locations_v3_search.json", "r", encoding='utf-8') as file:
#     text = file.read()
#     resp = json.loads(text)
    # print(resp['sr'][0])
    # dict1 = resp['sr'][1]
    # region_type = dict1.get('type')
    # print(region_type)
    # print(resp['sr'][0]['regionNames']['shortName'])
    # for key, value in resp['sr'][0].items():
    #     print(key)
    #     print(value)
    # locations_dict = {}
    # for region in resp['sr']:
    #     for key, value in region.items():
    #         if value == 'CITY':
    #             # print(region['regionNames']['shortName'])
    #             # print(region['regionNames'].get('shortName'))
    #             # print(region['gaiaId'])
    #             city_name = region['regionNames'].get('shortName')
    #             city_id = region['gaiaId']
    #             locations_dict[city_name] = city_id
    # print(locations_dict)