class LNode:
    def __init__(self,x=None):
        self.data=x
        self.next=None
def add(h1,h2):
    if h1 is None:
        return h2
    if h2 is None:
        return h1
    p1=h1
    p2=h2
    resultHead=LNode(0)
    p=resultHead
    c=0
    sums=0
    tmp=None
    while p1 and p2:
        sums=p1.data+p2.data+c
        tmp=LNode(sums%10)
        c=sums//10
        p.next=tmp
        p=p.next
        p1=p1.next
        p2=p2.next
    if p1 is None:
        while p2:
            sums=p2.data+c
            tmp=LNode(sums%10)
            c=sums//10
            p.next=tmp
            p=p.next
            p2=p2.next
    if p2 is None:
        while p1:
            sums=p1.data+c
            tmp=LNode(sums%10)
            c=sums//10
            p.next=tmp
            p=p.next
    if c==1:
        tmp=LNode(1)
        p.next=tmp
    return  resultHead.next

def generate():
    i = 1
    head = LNode(1)
    tmp = None
    cur = head
    while i < 7:
        tmp = LNode()
        if i % 2 == 0:
            tmp.data = i + 1
        elif i % 3 == 0:
            tmp.data = i - 2
        else:
            tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = cur.next
        i += 1
    return head

def printList(head):
    cur=head
    while cur:
        print(cur.data,end=" ")
        cur=cur.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def addTwoNumbers( l1, l2) :
    f = LNode(0)  # 定义输出链表的第一个节点
    p = f  # p类似于指针，代表输出链表的第一个节点
    carry = 0  # 进位
    while l1 or l2:  # 判断l1和l2两个链表是否都结束了
        x = l1.data if l1 else 0  # 如果l1链表没结束那么将l1的值给x，否则0给x
        y = l2.data if l2 else 0
        res = x + y + carry  # 与进位一起相加的结果
        carry = res // 10  # 检查是否有进位
        p.next = LNode(res % 10)  # 下一个节点的地址给此时的节点
        p = p.next  # 这时p指向的是上一行定义的节点
        l1 = l1.next if l1 else 0  # 如果链表l1没有了，那么要给l1赋值0，否则会报l1没有next属性的错
        l2 = l2.next if l2 else 0
    if carry > 0:  # 如果到最后还有进位，那么还要新建个节点记录进位的值
        p.next = LNode(1)
    return f.next  # 返回的链表一定要从定义的输出链表f的第二个节点开始


if __name__ == '__main__':
    h1 = generate()
    h2=generate()
    printList(h1)
    print()
    printList(h2)
    print()
    print("-"*20)

    # n = addTwoNumbers(h1, h2)
    n=add(h1,h2)
    printList(n)

    # printList(h1)
