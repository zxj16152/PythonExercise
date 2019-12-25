import random


class SNode:
    def __init__(self,key=None,value=None):
        self.key=key
        self.maxIndex=-1
        self.link=[]
        self.value=value

class SkipList:
    def __init__(self,size=8,larger=65535):
        self.size=size
        self.tail=SNode()
        self.head=SNode()
        self.last=[]
        self.tail.key=larger
        for i in range(self.size):
            self.head.link.append(self.tail)

        self.MAX_RAND=self.size

    def randomDispenseLevel(self):
        level=1
        while random.randint(0,1)==1:
            level+=1
        return level if level<=self.MAX_RAND else self.MAX_RAND


