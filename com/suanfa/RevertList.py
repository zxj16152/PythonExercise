class Node:
    def __init__(self,x):
     self.val=x
     self.next=None


def reverse(head):
    if (head or head.next is None):
        return head
    p=head.next
    q=None
    head.next=None
    while p:
        pr=p.next
        p.next=q
        q=p
        p=pr
    head.next=q
    return head

def reverse1(head):
    # newH=None
    while head is not None:
        # print("-head--%d---"%head.val)
        temp=head.next
        newH=head
        head=temp
        # print( "---%d---"%newH.val)
    return newH

    def Reverse(phead):
        if phead or phead.next is None:  # 判断是否为空表
            return phead
        newhead = None  # 建立新链表
        while phead:
            temp = phead.next  # 先将原链表的第二个节点保存在temp中
            phead.next = newhead  # 将原链表的第一个节点变为新链表的最后一个节点
            newhead = phead
            phead = temp
        return newhead


def reverseLinkedList(head):
    if head or head.next is None:
        return head
    else:
        temp=head.next
        newhead=reverseLinkedList(head.next)
        temp.next=head
        head.next=None
        print(newhead.val+"------")
        return newhead




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

   linked_list = reverseLinkedList(n1)
   # linked_list = reverse(n1)
   # p=linked_list
   # p=n1
   # p = reverse1(n1)
   p = reverse(n1)
   while p:
       print(p.val)
       p=p.next

if __name__ == '__main__':
    main()
