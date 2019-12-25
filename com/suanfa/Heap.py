class Heap:
     def __init__(self):
         self.__arr=[None]


     def insert(self,data):
         self.__arr.append(data)

         i= len(self.__arr)-1
         while (i//2>0 and self.__arr[i]>self.__arr[i//2]):
             self.__arr[i],self.__arr[i//2]=self.__arr[i//2],self.__arr[i]
             i=i//2

     def breathTravel(self):
         print(self.__arr)

     def removeMax(self):
         if len(self.__arr)<2 :
             return
         self.__arr[1]=self.__arr[-1]
         del self.__arr[-1]
         self.heapify(self.__arr,1)

     def heapify(self,arr,i):
         n=len(arr)-1
         while True:
             maxPos=i
             if i*2<=n and arr[i]<arr[2*i]:
                 maxPos=i*2
             if (i*2+1)<=n and arr[maxPos]<arr[2*i+1]:
                 maxPos=i *2+1
             if maxPos==i:
                 break
             arr[i],arr[maxPos]=arr[maxPos],arr[i]
             i=maxPos




if __name__ == '__main__':
    heap = Heap()
    heap.insert(33)
    heap.insert(34)
    heap.insert(17)
    heap.insert(16)
    heap.insert(22)
    heap.insert(5)

    #
    # heap.insert(9)
    # heap.insert(5)
    # heap.insert(6)
    # heap.insert(7)
    # heap.insert(8)
    # heap.insert(2)
    # heap.insert(22)
    # heap.insert(15)
    # heap.insert(1)
    heap.breathTravel()
    heap.removeMax()
    heap.breathTravel()
