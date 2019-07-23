def test():
    a,b=0,1
    for i in range(10):
        yield b
        a,b=b,a+b



test=test();
print(next(test))
print(next(test))
print(next(test))
print(next(test))
print(next(test))
print(next(test))
print(next(test))
print(next(test))
print(next(test))
print(next(test))
print(next(test))
