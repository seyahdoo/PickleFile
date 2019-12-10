
from picle_file import PickleFile


class Person:
    def __init__(self):
        self.name = "jonathan"
        self.surname = "joaster"
        self.age = 22

    def __str__(self):
        return "{}:{}:{}".format(self.name, self.surname, self.age)


# magic user
m = PickleFile("magic_pickle_data")

p = Person()
p.name = "hello"
m.person = p

print(m.person)

m.var = "variable"
print(m.var)
