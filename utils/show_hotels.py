# TODO найти в деталях адрес и взять от туда страну, город, адрес
from loader import bot
import re
from keyboards.inline_keyboards.hotel_details import hotel_details_keyboard


def show_hotel(hotel: dict, chat_id: int) -> None:
    """
    Выдача информации по отелю.

    :param hotel: словарь отеля
    :type hotel: dict
    :param chat_id: id чата
    :type chat_id: int
    :return: None
    """

    hotel_name = hotel['name']
    country = 'n/d'
    city = 'n/d'
    street_adr = 'n/d'
    distance = hotel['from_center']
    price_per_night = hotel['price']
    total_price = hotel['total_price']
    hotel_id = hotel["id"]
    # f'*Расположен по адресу:* {country},\t{city},\t{street_adr}\n' \
    hotel_description = f'*Отель:* {hotel_name}\n' \
                        f'*Расстояние от центра (км):* {distance}\n' \
                        f'*Цена за ночь:* ${price_per_night}\n' \
                        f'*Общая стоимость:* ${total_price}' \

    hotel_description = re.sub(r'-', r'[\-]', hotel_description)
    hotel_description = re.sub(r'[.]', r'[\.]', hotel_description)
    hotel_description = re.sub(r'[(]', r'[\(]', hotel_description)
    hotel_description = re.sub(r'[)]', r'[\)]', hotel_description)

    bot.send_message(chat_id, hotel_description,
                     reply_markup=hotel_details_keyboard(hotel_id, False, False),
                     parse_mode='MarkdownV2')
