from weather import Weather
from tinydb import TinyDB, Query

weather = Weather(unit='c')
db = TinyDB('db.json')


def put_to_db(location, weather_string):
    weather_lst = weather_string.split(':')
    db.insert({'location': location,               
               'weather': weather_lst})


def get_from_db(location):
    Key = Query()
    return db.search(Key.location == location)


def get_weather(location):
    location = weather.lookup_by_location(location)
    forecasts = location.forecast()
    result = []
    for forecast in forecasts:
        result.append(forecast.text())
        result.append(forecast.date())
        result.append(forecast.high())
        result.append(forecast.low())
    return ':'.join(result)
