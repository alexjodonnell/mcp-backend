from datetime import datetime


def convert(date_time):
    date_time = date_time[0:26]
    return datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S.%f').timestamp() * 1000
