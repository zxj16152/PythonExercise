def function1(n,m):
    return function2(3.4)

def function2(n):
    if n>0:
        return 1
    elif n==0:
        return 0
    else:
        return -1

print(function1(1,4))