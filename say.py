import telebot
import gtts
import datetime
import os

current_path = os.path.abspath(os.getcwd())

v = "2098675499:AAH_lNi3QVlfsFt8za-IkvT0thvS9L3M8zk"


my_bot = telebot.TeleBot(v)
@my_bot.message_handler(commands=["start", "старт"])
def say_hello(message):
    my_bot.send_message(message.chat.id, "чупапи")

@my_bot.message_handler(content_types="text")
def say_any(message):
    text = message.text
    say = gtts.gTTS(text, lang = "en")
    file_name = datetime.datetime.today()
    say.save(f"{file_name}.mp3")
    finale_path = f"{current_path}/{file_name}.mp3"
    audio_file = open(finale_path, 'rb')
    my_bot.send_message(message.chat.id, "готово")
    my_bot.send_audio(message.chat.id, audio_file)


@my_bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('а', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    my_bot.send_message(message.chat.id, 'кхъ', reply_markup=keyboard)

print("a")
my_bot.infinity_polling()
