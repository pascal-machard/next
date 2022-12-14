from datetime import datetime


class like:
    def __init__(self, value, user, date):
        self.value = value
        self.user = user
        self.date = datetime.strptime(date, '%d/%m/%y %H:%M:%S')

