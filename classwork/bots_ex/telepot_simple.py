import time
import random
import datetime
import telepot
from telepot.loop import MessageLoop


def get_news():
    pass


def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print('Got command: %s' % command)

    if command == '/roll':
        bot.sendMessage(chat_id, random.randint(1,6))
    elif command == '/time':
        bot.sendMessage(chat_id, str(datetime.datetime.now()))
    elif command == '/news':
        for piece in get_news()[:-3]:
            bot.sendMessage(chat_id, piece)
    else:
        bot.sendMessage(chat_id, "got it, but can't understand")


bot = telepot.Bot('your_token')

MessageLoop(bot, handle).run_as_thread()
print('I am listening ...')

while 1:
    time.sleep(10)
