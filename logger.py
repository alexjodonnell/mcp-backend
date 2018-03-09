from datetime import datetime


class Logger:
    def __init__(self, print_val):
        self.print_val = print_val

    def log(self, uri):

        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_line = '{} {}\n'.format(date, uri)
        with open('log.log', 'a') as file:
            file.write(log_line)

        if self.print_val:
            print(log_line, end='')
