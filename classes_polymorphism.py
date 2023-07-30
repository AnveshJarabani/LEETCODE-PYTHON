from abc import ABCMeta, abstractmethod

x = [1, 2, 3]
for i in x[:]:
    x.append(i + 1)
    print(x)


class Jungle(metaclass=ABCMeta):
    def __init__(
        self,
        name="Unknown",
    ):
        self.name = name

    def introduce(self):  # no need to add name here again.
        print(f"Welcome to the {self.name} Jungle")

    @abstractmethod
    def scarysound(self):
        ...


class Bungle:
    def __init__(
        self,
        name="Unknown",
    ):
        self.name = name

    def introduce(self):
        print(f"welcome to the {self.name} Bungle")


""" 
This is polymorphism because the method "introduce" is local to two different
classes but python allows for same method to be used in different classes. 
"""

amazon = Jungle("Amazon")
bamazon = Bungle("Bamazon")
amazon.introduce()
bamazon.introduce()


class RateJungle(Jungle):
    def __init__(self, name, rating=None):
        super(RateJungle, self).__init__(name)  # inheriting the constructor of class
        self.rating = rating

    def printRating(self):
        print(f"The Jungle rating is {self.rating} with {self.name}")


r = RateJungle("Meher", 3)
r.printRating()
r.introduce()


class Insect(Jungle):
    def scarysound(self):
        print("insects don't care about scary sounds")


i = Insect()
i.scarysound()
