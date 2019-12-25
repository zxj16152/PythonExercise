class LNode:
    def __init__(self,x):
        self.data=x
        self.next=None
    def reverse0(self,head):
        if head==None or head.next==None:
            return
        pre=None
        cur=None
        next=None
        while cur.next:
            next=cur.next
            cur.next=pre
            pre=cur
            cur=cur.next
        cur.next=pre
        head.next=cur

    def reverse(self,head):
        if head==None or head.next==None:
            return
        cur=head
        tmp=None
        newHead=None
        while cur:
            tmp=cur.next
            cur.next=newHead
            newHead=cur
            cur=tmp
        return newHead
    def reverse2(self,head):
        if head or head.next:
            return head
        Node=None
        while head:
            p=head
            head=head.next
            p.next=Node
def recursiveReverse(self,head):
        if head is None or head.next is None:
            return head
        else:
            newHead=recursiveReverse(head.next)
            head.next.next=head
            head.next=None
            return newHead


def reverse3(head):
    if head is None or head.next is None:
        return head
    cur=None
    next=None
    cur=head.next.next
    while cur:
        next=cur.next
        cur.next=head
        head.next=cur


if __name__ == '__main__':
    head=LNode(1)
    n1=LNode(2)
    n2=LNode(3)
    n3=LNode(4)
    n4=LNode(5)
    n5=LNode(6)
    n6=LNode(7)
    n7=LNode(8)
    head.next=n1
    n1.next=n2
    n2.next=n3
    n3.next=n4
    n4.next=n5
    n5.next=n6
    n6.next=n7
