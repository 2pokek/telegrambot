import telebot, random
from telebot import types

token = '5710747233:AAHq9AMST_QkGRrpGU57zDMsamw2Ur2OOaU'
bot = telebot.TeleBot(token)
e = 'kek'
z = 'ke'


def create_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    zodiac_btn = types.InlineKeyboardButton(text="Узнасть знак Зодиака", callback_data='1')
    cookies_btn = types.InlineKeyboardButton(text="Печенька с предсказанием", callback_data='2')
    keyboard.add(zodiac_btn)
    keyboard.add(cookies_btn)
    return keyboard


@bot.message_handler(commands=['start'])
def start_bot(message):
    keyboard = create_keyboard()
    bot.send_message(
        message.chat.id,
        "Добрый день! Выберите, что Вы хотите",
        reply_markup=keyboard
    )


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    keyboard = create_keyboard()
    if call.message:
        if call.data == "1":
            bot.send_message(call.message.chat.id, 'Какого числа у тебя День рождения?(Цифрами и без нуля в начале)')
            bot.register_next_step_handler(call.message, zodiac1_sign)
        if call.data == "2":
            x = random.randint(1, 3)
            if x == 1:
                a = 'Вас ждет что-то хорошее'
            elif x == 2:
                a = 'Вас ждет успех'
            elif x == 3:
                a = 'Вы скоро обрадуетесь'
            bot.send_message(call.message.chat.id, f'{a}')


@bot.message_handler(content_types='text')
def zodiac1_sign(message):
    global z
    z = int(message.text)
    bot.send_message(message.chat.id, 'В каком месяце у тебя День рождения?(Цифрами и без нуля в начале )')
    bot.register_next_step_handler(message, zodiac2_sign)


@bot.message_handler(content_types='text')
def zodiac2_sign(message):
    global e
    e = int(message.text)
    bot.register_next_step_handler(message, zodiac3_sign)

@bot.message_handler(content_types='text')
def zodiac3_sign(message):
    if e == 1 and z <= 19:
        bot.send_message(message.chat.id, "Вы Козерог")
    elif e == 12 and z >= 22 and z <= 31:
        bot.send_message(call.message.chat.id, "Вы Козерог")
    elif e == 1 and z >= 20 and z <= 29:
        bot.send_message(call.message.chat.id, "Вы Водолей")
    elif e == 2 and z >= 1 and z <= 19:
        bot.send_message(call.message.chat.id, "Вы Водолей")
    elif e == 2 and z >= 20 and z <= 31:
        bot.send_message(call.message.chat.id, "Вы Рыбы")
    elif e == 3 and z >= 1 and z <= 20:
        bot.send_message(call.message.chat.id, "Вы Рыбы")
    elif e == 3 and z >= 21 and z <= 30:
        bot.send_message(call.message.chat.id, "Вы Овен")
    elif e == 4 and z >= 1 and z <= 20:
        bot.send_message(call.message.chat.id, "Вы Овен")
    elif e == 4 and z >= 21 and z <= 31:
        bot.send_message(call.message.chat.id, "Вы Телец")
    elif e == 5 and z >= 1 and z <= 20:
        bot.send_message(call.message.chat.id, "Вы Телец")
    elif e == 5 and z >= 21 and z <= 30:
        bot.send_message(call.message.chat.id, "Вы Близнецы")
    elif e == 6 and z >= 1 and z <= 20:
        bot.send_message(call.message.chat.id, "Вы Близнецы")
    elif e == 6 and z >= 21 and z <= 31:
        bot.send_message(call.message.chat.id, "Вы Рак")
    elif e == 7 and z >= 1 and z <= 22:
        bot.send_message(call.message.chat.id, "Вы Рак")
    elif e == 7 and z >= 23 and z <= 31:
        bot.send_message(call.message.chat.id, "Вы Лев")
    elif e == 8 and z >= 1 and z <= 22:
        bot.send_message(call.message.chat.id, "Вы Лев")
    elif e == 8 and z >= 23 and z <= 30:
        bot.send_message(call.message.chat.id, "Вы Дева")
    elif e == 9 and z > 1 and z <= 22:
        bot.send_message(call.message.chat.id, "Вы Дева")
    elif e == 9 and z >= 23 and z <= 31:
        bot.send_message(call.message.chat.id, "Вы Весы")
    elif e == 10 and z >= 1 and z <= 22:
        bot.send_message(call.message.chat.id, "Вы Весы")
    elif e == 10 and z >= 23 and z <= 30:
        bot.send_message(call.message.chat.id, "Вы Скорпион")
    elif e == 11 and z >= 1 and z <= 22:
        bot.send_message(call.message.chat.id, "Вы Скорпион")
    elif e == 11 and z >= 23 and z <= 31:
        bot.send_message(call.message.chat.id, "Вы Стрелец")
    elif e == 12 and z >= 1 and z <= 21:
        bot.send_message(call.message.chat.id, "Вы Стрелец")
    else:
        bot.send_message(call.message.chat.id, "Вы Где-то ошиблись")


if __name__ == "__main__":
    bot.polling(none_stop=True)
