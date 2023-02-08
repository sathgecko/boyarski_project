import json
import re
from typing import List, Optional
# from . import connect_rapid_api
from loader import rapid_api
from logger_config import logger
import requests



def request_photo(hotel_id: int) -> Optional[List]:
    url = "https://hotels4.p.rapidapi.com/properties/v2/get-summary"

    payload = {
        "currency": "RUB",
        "eapid": 1,
        "locale": "ru_RUS",
        "siteId": 300000001,
        "propertyId": "45773013"
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "06dd932f31msh0a52e2bdec9c858p132b0cjsnd04a260d0e20",
        "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
    }

    # response = requests.request("POST", url, json=payload, headers=headers)

    # print(response.text)
    # if response:
    #     resp_json = json.loads(response.text)
    #     with open("v2_get-summary_45773013.json", "w") as file:
    #         json.dump(resp_json, file, indent=4)  # записываем файл для проверки и сохранения в БД
    with open("v2_get-summary_45773013.json", "r") as file:
        text = file.read()
        resp = json.loads(text)
    if resp:
        hotel_images = [] # список изображений по ID отеля
        # print(resp['data']['propertyInfo']['summary']['id']) # id hotel
        # print(resp['data']['propertyInfo']['summary']['location']['address'].get('addressLine')) # adress
        # print(resp['data']['propertyInfo']['propertyGallery']['images'][0]['image']['url']) # image 0
        for elem in resp['data']['propertyInfo']['propertyGallery']['images']:
            hotel_images.append(elem['image']['url'])
        print(hotel_images)
        address = resp['data']['propertyInfo']['summary']['location']['address'].get('addressLine')
        print(address)


        # for hotel in resp['data']['propertySearch']['properties']:

    # if response:
    #     resp_json = json.loads(response.text)
    #     with open("v2_get-summary_45773013.json", "w") as file:
    #         json.dump(resp_json, file, indent=4)  # записываем файл для проверки и сохранения в БД


        # resp_json = json.loads(response.text)
        #
        # hotel_images = resp_json['hotelImages']
        # hotel_images_length = len(hotel_images)
        #
        # photos_links = []
        #
        # for elem in range(0, 10):
        #     # Хардкодом ограничиваю количество фото до 10
        #     if elem > hotel_images_length:
        #         break
        #
        #     base_url = hotel_images[elem]['baseUrl']
        #     photo_url = re.sub(r'{size}', 'y', base_url)
        #     photos_links.append(photo_url)
        #     elem += 1
        #
        # return photos_links
request_photo('45773013')