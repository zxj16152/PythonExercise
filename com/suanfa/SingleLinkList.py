class Node(object):
    def __init__(self,val):
        self.val=val
        self.next=None

class SingleLinkList(object):
    def __init__(self,node=None):
        self.__head=node

    def is_empty(self):
        return self.__head

    def length(self):
        cur=self.__head
        count=0
        while cur !=None:
            count+=1
            cur=cur.next
        return count

    def travel(self):
        cur=self.__head
        while cur != None:
            print(cur.val,end=' ')
            cur=cur.next

    def add(self,item):
        node=Node(item)
        node.next=self.__head
        self.__head=node

    def append(self,item):
        node=Node(item)
        if self.is_empty():
            self.__head=node
        else:
            cur=self.__head
            while cur.next !=None:
                cur=cur.next
            cur.next=node

    def insert(self,pos,iterm):
        if pos<=0:
            self.add(iterm)
        elif pos>self.length()-1:
            self.append(iterm)
        else:
            per=self.__head
            count=0
            while count<pos-1:
                count+=1
                per=per.next
            node=Node(iterm)
            node.next=per.next
            per.next=node

    def remove(self,item):
        cur=self.__head
        pre=None
        while cur !=None:
            if cur.val==item:
                if cur ==self.__head:
                    self.__head=cur.next
                else:
                    pre.next=cur.next
                    # cur=cur.next
                    print(cur.val)
                break

            else:
                pre=cur
                cur=cur.next



def main():
   n1=Node(1)
   n2=Node(2)
   n3=Node(3)
   n4=Node(4)
   n5=Node(5)
   n1.next=n2
   n2.next=n3
   n3.next=n4
   n4.next=n5
   list = SingleLinkList(n1)

   list.add(19)
   list.remove(3)
   list.travel()

if __name__ == '__main__':
    main()
