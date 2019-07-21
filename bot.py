import telebot
import requests
import re
from telebot.types import Message

TOKEN = '955405255:AAF_gkRD6NoxyKg9_cKRdZbwGbBcdXstcIw'

bot = telebot.TeleBot(TOKEN)


def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url


def get_image_url():
    allowed_extension = ['jpg', 'jpeg', 'png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url


@bot.message_handler(commands=['photo'])
def return_pic(message):
    bot.send_photo(message.chat.id, get_image_url(), reply_to_message_id=message.message_id)

bot.polling()
