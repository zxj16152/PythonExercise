import sys

class Animal:
    def eat(self):
        print("吃============")
class Dog(Animal):
    def __init__(self,name,age):
        self.__name=name;
        self.__age=age;

    def set_name(self,name):
        self.__name=name;
    def get_name(self,name):
        return name
    def set_age(self,age):
        self.__age=age

    def eat(self):
        # Animal.eat(self)
        super().eat()
        print("狂吃")

    def __str__(self):
        return  str(self.__age) + " " + self.__name;
    def __del__(self):
        print("----over")


dog1 = Dog("tom", 10)
dog1.eat()
print("------------")