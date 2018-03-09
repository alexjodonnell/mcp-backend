from datetime import datetime


class Logger:
    def __init__(self):
        self.file = open('log.log', 'w+')

    def log(self, uri):
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.file.write('{} {}\n'.format(date, uri))
