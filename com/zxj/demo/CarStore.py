class CarStore(object):
    def order(self,money):
        if money >50000:
            return Car()

class Car(object):
    name=0
    @classmethod
    def move(cls):
        print("paodong")
    @staticmethod
    def printmethod():
        print("===============")


car_store = CarStore()
car = car_store.order(600000)
print(Car.name)