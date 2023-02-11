# TODO разобраться с запросом по параметру page
import json
from typing import List, Optional
from logger_config import logger
import requests
from . import connect_rapid_api_post
from loader import rapid_api
# import re
# import datetime
def get_address(hotel_id):
    """Получение адреса с API, используется на 103 и 108 строчке при необходимости"""
    url2 = "https://hotels4.p.rapidapi.com/properties/v2/get-summary"
    req_params2 = {
        "currency": "RUB",
        "eapid": 1,
        "locale": "ru_RUS",
        "siteId": 300000001,
        "propertyId": hotel_id
    }

    response2 = connect_rapid_api_post(url2, rapid_api, req_params2)
    # print(response2)
    resp_json2 = json.loads(response2.text)
    # print(resp_json2)
    address = resp_json2['data']['propertyInfo']['summary']['location']['address']['addressLine']
    # print(address)
    return address

@logger.catch
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
    print(search_data)
    command = search_data.get('command', None)
    if command == 'lowprice':
        sort_order = 'PRICE_LOW_TO_HIGH '
    # elif command == 'highprice':
    #     sort_order = 'PRICE_HIGHEST_FIRST'
    elif command == 'bestdeal':
        sort_order = 'DISTANCE'
    else:
        sort_order = 'RECOMMENDED'
    # One  # of  # the # following:
    # PRICE_RELEVANT(Price + our  # picks) |
    # REVIEW(Guest  # rating) |
    # DISTANCE(Distance # from downtown) |
    # PRICE_LOW_TO_HIGH(Price) |
    # PROPERTY_CLASS(Star  # rating) |
    # RECOMMENDED(Recommended)
    # Ex: "sort": "RECOMMENDED"

    checkin_date = search_data['checkin_date']
    checkout_date = search_data['checkout_date']

    req_params = {"currency": "RUB",
                  "eapid": 1,
                  "locale": "ru_RUS",
                  "siteId": 300000001,
                  "destination": {"regionId": search_data.get('location', None)},
                  "checkInDate": {
                      "day": search_data['checkin_date'].date().day,
                      "month": search_data['checkin_date'].date().month,
                      "year": search_data['checkin_date'].date().year
                  },
                  "checkOutDate": {
                      "day": search_data['checkout_date'].date().day,
                      "month": search_data['checkout_date'].date().month,
                      "year": search_data['checkout_date'].date().year
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

    response = connect_rapid_api_post('https://hotels4.p.rapidapi.com/properties/v2/list', rapid_api, req_params)
    # print(response)

    if response:
        resp_json = json.loads(response.text)
        hotels_list = []
        for hotel in resp_json['data']['propertySearch']['properties']:
            price = hotel['price']['lead'].get('amount', 'n/d')
            if not isinstance(price, str):
                total_price = price * (checkout_date - checkin_date).days
            else:
                total_price = 'n/d'
            # address = get_address(hotel['id'])
            distance = (float(hotel['destinationInfo']['distanceFromDestination']['value']) * 161) / 100 # мили в км
            new_hotel = {
                'id': hotel['id'],
                'name': hotel['name'],
                # 'address': 'Адрес при бронировании',#address
                'from_center': round(distance, 2),
                'price': round(hotel['price']['lead']['amount'], 2),
                'total_price': round(total_price, 2)
            }

            hotels_list.append(new_hotel)
        print(hotels_list)
        return hotels_list