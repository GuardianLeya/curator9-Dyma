import telebot

bot = telebot.TeleBot('6845525104:AAFHhKHM5scQi2qVt-NlQPkFpbpP5IAhfcM')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id,
                     'Привет ✌🏿, я бот RobertAlbert\n*Вот, то что я могу на данный момент:* \n[/info](/info) Инфоромация обо мне\n[/text](/text) Выведет текст\n[/smile](/smile) Выведет смайл\n[/link](/link) Выведет ссылку',
                     parse_mode='Markdown')


@bot.message_handler(commands=['info'])
def main(message):
    bot.send_message(message.chat.id,
                     'Привет ещё раз ✋🏿, друг, я детище начинающего разработчика Python Дмитрия👨🏻‍💻',
                     parse_mode='Markdown')


@bot.message_handler(commands=['text'])
def main(message):
    bot.send_message(message.chat.id, '_lorem ipsum dolor sit amet_', parse_mode='Markdown')


@bot.message_handler(commands=['smile'])
def main(message):
    bot.send_message(message.chat.id, '🤡', parse_mode='Markdown')


@bot.message_handler(commands=['link'])
def main(message):
    bot.send_message(message.chat.id, '[DIRTY DIANA](https://music.yandex.ru/album/11560809/track/69226088)',
                     parse_mode='Markdown')


bot.infinity_polling()
