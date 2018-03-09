from datetime import datetime


class Logger:
    def __init__(self, print):
        self.print = print

    def log(self, uri):
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_line = '{} {}\n'.format(date, uri)
        with open('log.log', 'w+') as file:
            file.write(log_line)

        if self.print:
            print(log_line, end='')
