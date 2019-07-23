class Animal():
    def __init__(self, name):
        self.name1 = name
        print("init")
        print("%s" % (name))
        # self.__init__()

    def __new__(cls, *args, **kwargs):
        print("new")
        return object.__new__(cls)

    def __getattribute__(self, item):
        print("getattribute")
        if item.startswith('name'):
            print(item)
            return 'haha'
        else:
            return object.__getattribute__(self,item)
    def eat(self):
        print('----------eat----------')


animal = Animal("an")
print(__name__)