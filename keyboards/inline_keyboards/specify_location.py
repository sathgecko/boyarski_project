from telebot import types


def specify_location_keyboard(locations_dict: dict) -> types.InlineKeyboardMarkup:
    """
    Создаёт клавиатуру для выбора конкретной локации из списка

    :return: keyboard
    :rtype: InlineKeyboardMarkup
    """

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    for key in locations_dict.keys():
        # print(key)
        # keyboard.add(types.InlineKeyboardButton(text=key, callback_data=key + '|' + locations_dict[key]))
        keyboard.add(types.InlineKeyboardButton(text=key, callback_data=locations_dict[key]))

    try_again = types.InlineKeyboardButton(text='↩Начать сначала', callback_data='TRY_AGAIN')
    stop_search = types.InlineKeyboardButton(text='🛑Прервать поиск', callback_data='CANCEL')

    keyboard.add(try_again)
    keyboard.add(stop_search)

    return keyboard
