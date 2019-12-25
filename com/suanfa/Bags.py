import math
import sys

maxW=-1
bag=[]
def backpack(i,cw,items,w): #i 第几个物品，包中物品的重量，items包中物品，w包的承重
    global maxW,bag
    if cw ==w or i==len(items):
        if cw>maxW:
           maxW=cw
           bag.append(maxW)
        return
    backpack(i+1,cw,items,w)

    if(cw+items[i]<=w):
        bag.append(items[i])
        backpack(i+1,cw+items[i],items,w)



def f(x):
    if x==0:
        return 0
    res=sys.maxsize
    if (x>=5):
        res=min(f(x-5)+1,res)
    if (x>=2):
        res=min(f(x-2)+1,res)
    if (x>=7):
        res=min(f(x-7)+1,res)
    return res



if __name__ == '__main__':
    items=[2,2,4,6,3]
    backpack(0,0,items,10)
    print(maxW)
    print(bag)
    print(len(bag))
    print(f(27))
