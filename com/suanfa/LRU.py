from collections import deque


class LRU:
    def __init__(self,cacheSize):
        self.cacheSize=cacheSize
        self.queue=deque()
        self.hashSet=set()
    def isQueueFull(self):
        return len(self.queue)==self.cacheSize
    def enqueue(self,pageNum):
        if self.isQueueFull():
            self.hashSet.remove(self.queue[-1])
            self.queue.pop()
        self.queue.appendleft(pageNum)
        self.hashSet.add(pageNum)
    def accessPage(self,pageNum):
        if pageNum not in self.hashSet:
            self.enqueue(pageNum)
        elif pageNum!=self.queue[0]:
            self.queue.remove(pageNum)
            self.queue.appendleft(pageNum)
    def printQueue(self):
        while self.queue:
            print(self.queue.popleft(),end=" ")

if __name__ == '__main__':
    lru=LRU(3)
    lru.accessPage(1)
    lru.accessPage(2)
    lru.accessPage(3)
    lru.accessPage(4)
    lru.accessPage(5)
    lru.accessPage(7)
    lru.printQueue()