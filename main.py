#TODO решить вопрос со ссылкой забронировать (на данный момент стоит просто ссылка на сайт(hotel_details_keyboard))
# сделать запросы через connect_rapid_api
from loader import bot
import handlers
from telebot.custom_filters import StateFilter
from utils.set_bot_commands import set_default_commands

if __name__ == '__main__':
    bot.add_custom_filter(StateFilter(bot))
    set_default_commands(bot)
    bot.infinity_polling()
