from datetime import datetime


class Empty(Exception):
    pass

class ArrayQuequ(object):
    DEFAULT_CAPACITY=10

    def __init__(self,n=DEFAULT_CAPACITY):
        self._arr=[None]*(n+1)
        self._size=0
        self._front=0
        self._tail=0

    def __str__(self):
        return str(self._arr)

    def __len__(self):
        return len(self._arr)
    def __iter__(self):
        return iter(self._arr)
    def get_size(self):
        return self._size
    def get_capacity(self):
        return self.__len__()-1
    def is_empty(self):
        return self._size==0
    def get_front(self):
        return self._arr[self._front]
    def enqueue(self,e):
        if self.is_full():
            self.resize(self.get_capacity()*2)
        self._arr[self._tail]=e
        self._tail=(self._tail+1)%len(self._arr)
        self._size+=1
    def dequeue(self):
        if self.is_empty():
            raise Exception("Cannot dequeue from an empty queue")
        result=self._arr[self._front]
        self._arr[self._front]=None
        self._front=(self._front+1)%len(self._arr)
        self._size-=1
        if self._size<self.get_capacity()//2 and self.get_capacity()>1:
            self.resize(self.get_capacity()//2)
        return result


    def is_full(self):
        return (self._tail+1)%len(self._arr)==self._front

    def resize(self,new_capacity):
        new_arr=[None]*(new_capacity+1)
        for i in range(self._size):
            new_arr[i]=self._arr[(i+self._front)%len(self._arr)]

        self._arr=new_arr
        self._front=0
        self._tail=self._size

def main():
    quequ = ArrayQuequ()
    start_time = datetime.now()
    for i in range(5000000):
        quequ.enqueue(i)
    print('\n------------- 测试enqueue----------')
    print('queue: size={0},capacity={1}\n'.format(quequ.get_size(),quequ.get_capacity()))
    print('is_empty：', quequ.is_empty())
    print('is_full：', quequ.is_full())
    print('get_front：', quequ.get_front())

    for i in range(5000000):
        quequ.dequeue()
    last_time = datetime.now() - start_time
    print('\n---------测试dequeue----------')
    print('queue: size={0},capacity={1}\n'.format(quequ.get_size(),quequ.get_capacity()))
    print('is_empty：', quequ.is_empty())
    print('is_full：', quequ.is_full())
    print('get_front：', quequ.get_front())
    print('Loop_Queue运行时间：', last_time)


if __name__ == '__main__':
    main()