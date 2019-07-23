class Person(object):
    def __init__(self, name, age):
        self._name =name
        self._age=age

    @property
    def name(self):
        return self._name
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,age):
        self._age=age


    def play(self):
        if self._age<=16 :
            print("%s正在吃饭"%self._name)
        else:
            print("%s正在xuexi"%self._name)

def main():
    person = Person("农用套", 12)
    person.play()
    print(person.age)
    person.age=18
    print(person.age)
    person.play()
    # person.name="懂航"

if __name__ == '__main__':
    main()