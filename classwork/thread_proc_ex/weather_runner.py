from multiprocessing import (
    Queue,
    Process,
)

from weather_data import (
    put_to_db,
    get_from_db,
    get_weather,
)


def worker(location, q):
    """
    Get weather data and put it
    to the queue as is.
    """
    print("worker: %s" % location)
    q.put("%s|%s" % (location,
                     get_weather(location=location)))


def saver(q):
    """
    Save the data from the queue
    to the databasein format:
    <location>: [<list of weather info>].
    """
    while True:
        data = q.get()
        print("Got: %s" % data)
        location, weather_string = data.split('|')
        print("location: %s" % location)
        put_to_db(location=location,
                weather_string=weather_string)


def runner(locations):
    q = Queue()
    for location in locations:
        print("Process %s ..." % location)
        p = Process(target=worker, args=(location, q))
        p.start()       
    p = Process(target=saver, args=(q,))
    p.start()
    p.join()


if __name__ == '__main__':
    runner(locations=['kiev', 'rome',
                      'new york', 'paris'])