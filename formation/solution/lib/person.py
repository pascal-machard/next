from math import sqrt


class Person(object):

    def __init__(self, first_name="", last_name="", age=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return "{0} {1} {2} years".format(self.first_name, self.last_name, self.age)

    def inc_age(self):
        self.age += 1

    def who_is_it(self):
        return "I'm a person"