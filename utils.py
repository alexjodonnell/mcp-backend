from datetime import datetime
import time

import math


def convert(date_time):
    date_time = date_time[0:26]
    return datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S.%f').timestamp() * 1000 - 4*60*60*1000


def current_epoch():
    return time.time() * 1000


def convert_to_week(date_time, start_epoch, ms_per_week):
    epoch = convert(date_time)
    diff = epoch - start_epoch
    return int(math.floor(diff / ms_per_week))


def delay_until(start_epoch, return_week, ms_per_week):
    while True:
        if current_epoch() > start_epoch + (return_week * ms_per_week):
            return
