from datetime import datetime


class Logger:
    def __init__(self, print):
        self.file = open('log.log', 'w+')
        self.print = print

    def log(self, uri):
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_line = '{} {}\n'.format(date, uri)
        self.file.write(log_line)
        if self.print:
            print(log_line, end='')
