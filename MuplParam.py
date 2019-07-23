def sum (a,b,*args):
    result=a+b
    for temp in args:
        result+=temp
    return result

print(sum(23,12,32,30))
print(sum(1,2,3,4,5,5,))