import datetime

def phrase_date_time(name):
    x = datetime.datetime.now()
    date_time = f'{name} {x}'
    return date_time
