import json
import re
import datetime
from typing import List, Optional

import datetime as datetime

# from . import connect_rapid_api
from loader import rapid_api
from logger_config import logger
import requests


# @logger.catch
def request_hotels(search_data: dict, page: int = 1) -> Optional[List]:
    """
    Принимает на вход словарь с ответами пользователя, дополнительно его обрабатывает.
    Возвращает словарь с отелями, которые удовлетворяют условиям поиска.
    Если возникли проблемы с подключением к API, возвращает сообщение об ошибке.

    :param search_data: словарь с ответами пользователя.
    :type search_data: dict
    :param page: номер возвращаемой страницы
    :type page: int
    :return: список отелей или None
    :rtype: List
    """
    # print(search_data)
    # {'command': 'lowprice', 'location_type': 'CITY', 'location': '6054439',
    #  'checkin_date': datetime.datetime(2023, 2, 23, 0, 0), 'checkout_date': datetime.datetime(2023, 2, 28, 0, 0)}
    command = search_data.get('command', None) # команда lowprice
    if command == 'highprice':
        sort_order = 'PRICE_HIGHEST_FIRST'
    else:
        sort_order = 'PRICE'

    checkin_date = search_data['checkin_date']
    checkout_date = search_data['checkout_date']

    # "checkIn": datetime.datetime.strftime(checkin_date, '%Y-%m-%d'),
    # "checkOut": datetime.datetime.strftime(checkout_date, '%Y-%m-%d'),
    # "pageNumber": str(page),
    # "pageSize": "25",

    req_params = {"currency": "RUB",
                  "eapid": 1,
                  "locale": "ru_RUS",
                  "siteId": 300000001,
                  "destination": {"regionId": search_data.get('location', None)},
                  "checkInDate": {
                      "day": 10,
                      "month": 10,
                      "year": 2023
                  },
                  "checkOutDate": {
                      "day": 15,
                      "month": 10,
                      "year": 2023
                  },
                  "rooms": [{"adults": 1}],
                  "resultsStartingIndex": 0,
                  "resultsSize": 200,
                  "sort": sort_order,
                  "filters": {"price": {
                      "max": search_data.get('max_price', None),
                      "min": search_data.get('min_price', None)
                  }}
                  }
    url = 'https://hotels4.p.rapidapi.com/properties/v2/list'
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "06dd932f31msh0a52e2bdec9c858p132b0cjsnd04a260d0e20",
        "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
    }
    # response = requests.request("POST", url, json=req_params, headers=headers)
    # print(response)
    with open("properties_v2_vietnam.json", "r") as file:
        text = file.read()
        resp = json.loads(text)

    if resp:
        hotels_list = []
        # print(resp['data']['propertySearch']['properties'][0]['price']['lead']['amount']) # Цена
        print(resp['data']['propertySearch']['properties'][0]['propertyImage']['fallbackImage']['url']) # image1
        print(resp['data']['propertySearch']['properties'][0]['propertyImage']['image']['url']) # image2
        # print(resp['data']['propertySearch']['properties'][0]['sponsoredListing']['hotelImage']) # тоже image2
        # print(resp['data']['propertySearch']['properties'])
        for hotel in resp['data']['propertySearch']['properties']:
            price = hotel['price']['lead'].get('amount', 'n/d')
            if not isinstance(price, str):
                total_price = price * (checkout_date - checkin_date).days
            else:
                total_price = 'n/d'
            new_hotel = {
                        'id': hotel['id'],
                        'name': hotel['name'],
                        'address': 'n/d',
                        'from_center': 'n/d',
                        'price': round(hotel['price']['lead']['amount'], 2),
                        'total_price': round(total_price, 2)
                    }

            hotels_list.append(new_hotel)
        print(hotels_list)
        return hotels_list

    #     min_dist = search_data.get('min_dist', -1)
    #     max_dist = search_data.get('max_dist', -1)

    # if response:
    #     resp_json = json.loads(response.text)
    #     results = resp_json.get('data', None).get('body', None).get('searchResults', None).get('results', None)
    #
    #     hotels_list = []
    #     min_dist = search_data.get('min_dist', -1)
    #     max_dist = search_data.get('max_dist', -1)
    #
    #     for hotel in results:
    #         from_center = 'n/d'
    #
    #         for landmark in hotel['landmarks']:
    #             if landmark.get('label', None) == 'City center':
    #                 # Получаю расстояние до центра, убираю лишнее, перевожу во float, и перевожу из миль в км
    #                 from_center = round(float(re.sub(r'[^\d.]', '', landmark['distance'])) * 1.609, 1)
    #
    #         if command == 'bestdeal' and (from_center == 'n/d' or from_center < min_dist or from_center > max_dist):
    #             continue
    #
    #         price = hotel['ratePlan']['price'].get('exactCurrent', 'n/d')
    #
    #         if not isinstance(price, str):
    #             total_price = price * (checkout_date - checkin_date).days
    #         else:
    #             total_price = 'n/d'
    #
    #         new_hotel = {
    #             'id': hotel['id'],
    #             'name': hotel['name'],
    #             'address': hotel['address'],
    #             'from_center': from_center,
    #             'price': round(price, 2),
    #             'total_price': round(total_price, 2)
    #         }
    #
    #         hotels_list.append(new_hotel)

        # return hotels_list

v3_search_dict = {'command': 'lowprice', 'location_type': 'CITY', 'location': '6054439',
     'checkin_date': datetime.datetime(2023, 2, 23, 0, 0), 'checkout_date': datetime.datetime(2023, 2, 28, 0, 0)}
request_hotels(v3_search_dict)

checkin_date1 = v3_search_dict['checkin_date']
checkout_date1 = v3_search_dict['checkout_date']

first = datetime.datetime.strftime(checkin_date1, '%Y-%m-%d')
second = datetime.datetime.strftime(checkout_date1, '%Y-%m-%d')
print(f'Чекин {first}')
print(f'Чекаут {second}')


