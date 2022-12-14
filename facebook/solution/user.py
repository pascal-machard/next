class user:
    def __init__(self, name, mail, birthday):
        self.name = name
        self.mail = mail
        self.birthday = birthday

        self.active = True

        self.__posts = []
        self.__friends = {}

    def add_post(self, new_post):
        self.__posts.append(new_post)

    def number_of_post(self):
        return len(self.__posts)

    def add_friend(self, u):
        self.__friends[u.name] = u

    def number_of_friend(self):
        return len(self.__friends.items())

    def get_friend(self, pos):
        return self.__friends.items()[pos]

    def search_friend(self, param):
        return self.__friends[param]
