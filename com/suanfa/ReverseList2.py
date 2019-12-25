class Lnode():
    def __init__(self,x):
        self.data=x
        self.next=None

def findMidAndReverse(head):
    if head is None or head.next is None:
        return head
    fast=head
    slow=head
    slowPre=head
    while fast and fast.next:
        slowPre=slow
        slow=slow.next
        fast=fast.next.next

    slowPre=None
    return slow

def reverse0(head):
    if head is None or head.next is None:
        return head
    pre=head
    cur=head.next
    pre.next=None
    while cur:
        next=cur.next
        cur.next=pre
        pre=cur
        cur=next
    return pre

def reOder(head):
    if head or head.next:
        return head
    cur1=head.next
    mid=findMidAndReverse(head.next)
    cur2=reverse0(mid)
    while cur1.next:
        tmp1=cur1.next
        tmp2=cur2.next
        cur1.next=cur2
        cur2.next=tmp1
        cur2=tmp2
        cur1=tmp1
    cur1.next=cur2

def findLastK(head,k): #找到链表倒数第k个数
    if head is None:
        return head
    fast=head
    slow=head
    i =0
    while i<k and fast:
        fast=fast.next
        i+=1
    if i<k:
        return None
    while fast:
        slow=slow.next
        fast=fast.next
    return slow





def generate():
    i = 1
    head = Lnode(None)
    cur = head
    while i < 15:
        tmp = Lnode(0)
        tmp.data = i + 1
        tmp.next = None
        cur.next = tmp
        cur = cur.next
        i += 1
    # cur.next=head.next.next.next.next
    return head
def rotateK(head,k): #把链表右旋k个位置
    if head is None or head.next is None:
        return head
    fast=head.next
    slow =head.next
    i=0
    while i<k and fast:
        fast=fast.next
        i+=1
    if i < k:
        return
    while fast.next:
        fast=fast.next
        slow=slow.next
    tmp=slow
    slow=slow.next
    tmp.next=None
    fast.next=head.next
    head.next=slow
    return head

def isLoop(head):
    if head is None or head.next is None:
        return None
    slow=head.next
    fast=head.next
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            return slow
    return None

def findLoopNode(head,meetNode):
    first=head.next
    second=meetNode
    while first!=meetNode:
        first=first.next
        meetNode=meetNode.next
    return first

def reverse2(head):  #反转相邻两节点
    if head is None or head.next is None:
        return
    cur=head.next
    pre=head
    while cur and cur.next:
        next=cur.next.next
        pre.next=cur.next
        cur.next.next=cur
        cur.next=next
        pre=cur
        cur=next
    return head
def reverse3(head,k): #以k个元素为一组进行反转
    if head is None or head.next is None or k<3:
        return head
    i=1
    pre=head
    begin=head.next
    end=None
    pNext=None
    while begin:
        end=begin
        while i<k:
            if end.next:
                end=end.next
            else:
                return
            i+=1
        pNext=end.next
        end.next=None
        pre.next=reverse0(begin)
        begin.next=pNext
        pre=begin
        begin=pNext
        i=1
    return head




if __name__ == '__main__':
    l = generate()
    p=l
    i=0
    while p and i<20:
        print(p.data,end=" ")
        p=p.next
        i+=1
    print()
    print('--'*20)
    # n = reverse0(l)
    # while n:
    #     print(n.data,end=" ")
    #     n=n.next
    # print()
    # print('--'*20)
    # loop = isLoop(l)
    # print(loop.data)
    # print(findLoopNode(l, loop).data)
    # head = rotateK(l,3)
    # cur=head.next
    # while cur:
    #     print(cur.data,end=" ")
    n2 = reverse3(l,2)
    cur=n2
    while cur :
        print(cur.data,end=" ")
        cur=cur.next
    print()
    print('--'*20)



