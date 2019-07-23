def w1(func):
    print('---------111-------')
    def inner():
        print("-----权限验证1------")
        return 'i' + func() + 'i'
    return inner

def w2(func):
    print('---------222---------')
    def inner():
        print("-----权限验证2------")
        return 'j' + func() + 'j'
    return inner
@w1
@w2
def f1():
    print("-----f1-------")
    return 'hello'




print(f1())