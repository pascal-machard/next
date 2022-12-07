from math import sqrt

from formation.solution.lib.person import Person


class Client(Person):

    def __init__(self, first_name="", last_name="", age=0):
        super().__init__(first_name, last_name, age)

    def who_is_it(self):
        return "I'm a client"