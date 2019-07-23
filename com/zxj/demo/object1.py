class Cat:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return "%s的年龄是：%d" % (self.name, self.age)

        print("============")
    def eat(self):
        print("猫吃鱼")
    def drink(self):
        print("喝水")

    def introduce(self):
        print()


cat = Cat("hello ketty",10 )
cat.eat()
cat.drink()
cat.introduce()
print(cat)
