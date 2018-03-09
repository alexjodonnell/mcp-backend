from datetime import datetime
import time


def convert(date_time):
    date_time = date_time[0:26]
    return datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S.%f').timestamp() * 1000 - 4*60*60*1000


def current_epoch():
    return time.time() * 1000
