class Lnode():
    def __init__(self,x):
        self.data=x
        self.next=None

def merge(head1,head2): #合并两个链表
    if head1 is None or head1.next is None:
        return head2
    if head2 is None or head2.next is None:
        return head1
    cur1=head1.next
    cur2=head2.next
    head=None
    cur=None
    if cur1.data>cur2.data:
        head=head2
        cur=cur2
        cur2=cur2.next
    else:
        head=head1
        cur=cur1
        cur1=cur1.next
    while cur1 and cur2:
        pass


class Solution:
    def mergeTwoLists(self, l1: Lnode, l2: Lnode) -> Lnode:
        node=Lnode(0)
        l3=node
        while l1 or l2:
            x=l1.val if l1 else 9999999999999999
            y=l2.val if l2 else 9999999999999999
            if x<=y:
                node.next=Lnode(x)
                if l1!=None:
                    l1=l1.next
            else:
                node.next=Lnode(y)
                if l2!=None:
                    l2=l2.next
            node=node.next
        return l3.next
