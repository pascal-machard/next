from datetime import datetime

from facebook.like import like


class post:
    def __init__(self, title, content):
        self.title = title
        self.content = content

        self.__like = []

    def add_like(self, value, like_user, like_date):
        self.__like.append(like(value, like_user, like_date))

    def number_of_like(self):
        return len(self.__like)

    def get_like(self, param):
        result = []
        for like in self.__like:
            if like.value == param:
                result.append(like)
        return result

    def get_like_date(self, param):
        result = []
        for like in self.__like:
            if like.date.strftime("%d/%m/%y") == param:
                result.append(like)
        return result

