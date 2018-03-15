import time
import random
import datetime
import requests

from weather import Weather
from bs4 import BeautifulSoup

import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton


def get_weather(location):
    weather = Weather(unit='c')
    location = weather.lookup_by_location(location=
        f'({location["latitude"]},{location["longitude"]})')

    forecasts = location.forecast()
    city = location.location().city()
    results = []
    for f in forecasts:
        results.append(f'{city}: {f.date()} | {f.text()} | '
                       f'{f.high()} | {f.low()}')
    return results


def get_news():
    ycomb = "https://news.ycombinator.com/"
    soup = BeautifulSoup(requests.get(ycomb).content)
    return [f"{i.get_text()} ({i.get('href')})"
            for i in soup.findAll(
            "a", {"class": "storylink"})]


def handle(msg):
    chat_id = msg['chat']['id']
    location = msg.get('location', None)

    if location is not None:
        print(f"Got location: {location}")
        for day in get_weather(location=location):
            bot.sendMessage(chat_id, day)

    text = msg.get('text', None)

    if text is not None:
        print(f'Got text: {text}')
        if text == '/roll':
            bot.sendMessage(chat_id, random.randint(1,6))
        elif text == '/time':
            bot.sendMessage(chat_id, str(datetime.datetime.now()))
        elif text == '/news':
            for piece in get_news()[:3]:
                bot.sendMessage(chat_id, piece)
        elif text == '/key':
            bot.sendMessage(chat_id, 'sendind location by request...',
                            reply_markup=ReplyKeyboardMarkup(
                                keyboard=[
                                    [KeyboardButton(
                                        text='Location by request',
                                        request_location=True)]
                                ]
                        ))
        elif text == 'Location by request':
            bot.sendMessage(chat_id, 'Ok')
        else:
            bot.sendMessage(chat_id,
                            "got text command, "
                            "but can't understand")


bot = telepot.Bot('TOKEN')

MessageLoop(bot, handle).run_as_thread()
print('I am listening ...')

while 1:
    time.sleep(10)
