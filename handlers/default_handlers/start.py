from loader import bot
from telebot.types import Message
from keyboards.reply_keyboards.help import help_keyboard


@bot.message_handler(commands=['start', 'hello-world'])
def greetings(message: Message) -> None:
    """
    Функция-приветствие (команды /start и /hello-world)

    :param message: Объект сообщения.
    :type message: Message
    :return: None
    """

    bot.send_message(message.chat.id, 'Привет! Я найду для тебя лучшие отели на сайте hotels.com (кроме России) 🌍'
                                      'Чтобы начать, введи команду или введи /help для справки!',
                     reply_markup=help_keyboard())
