class Node:
    def __init__(self,item):
        self.item=item
        self.next=None

class SingleList:
    def __init__(self):
        self.__head=None

    def isEmpty(self):
        return self.__head is None

    def length(self):
        cur=self.__head
        count=0
        while cur :
            count+=1
            cur=cur.next
        return count

    def travel(self):
        cur=self.__head
        while cur :
            print(cur.item,end=" ")
            cur=cur.next
        print("")

    def add(self,item):
        node = Node(item)
        node.next=self.__head
        self.__head=node

    def append(self,item):
        node=Node(item)
        if self.isEmpty():
            self.__head=node
        else:
            cur=self.__head
            while cur.next :
                cur=cur.next
            cur.next=node

    def insert(self,pos,item):
        if pos<=0:
            self.add(item)
        elif pos>(self.length()-1):
            self.append(item)
        else:
            node=Node(item)
            count=0
            pre=self.__head
            while count<(pos-1):
                pre=pre.next
                count+=1
            node.next=pre.next
            pre.next=node

    def remove(self,item):
        cur=self.__head
        pre=None
        while cur :
            if cur.item==item:
                if not pre :
                    self.__head=cur.next
                else:
                    pre.next=cur.next
                break
            else:
                pre=cur
                cur=cur.next

    def find(self,item):
        cur=self.__head
        while cur:
            if cur.item==item:
                return True
            cur=cur.next
        return False

if __name__ == "__main__":
    ll = SingleList()
    ll.add(1)
    ll.add(2)
    ll.append(3)
    ll.insert(2, 4)
    print("length",ll.length())
    print(ll.find(3))
    ll.travel()
    ll.remove(1)
    ll.travel()

