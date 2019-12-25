class LNode:
    def __init__(self,x=None):
        self.data=x;
        self.next=None

def removeDup(head):
    if head is None or head.next is None:
        return
    outerCur=head.next
    innerCur=None
    innerPre=None
    while outerCur:
        innerCur=outerCur.next
        innerPre=outerCur
        while innerCur:
            if outerCur.data==innerCur.data:
                innerPre.next=innerCur.next
                innerCur=innerCur.next
            else:
                innerPre=innerCur
                innerCur=innerCur.next
        outerCur=outerCur.next

def generate():
    i = 1
    head = LNode()
    head.next = None
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

if __name__ == '__main__':

    print("删除节点前")
    head = generate()
    cur=head.next
    while cur:
        print(cur.data)
        cur=cur.next
    removeDup(head)
    print("删除节点后")
    cur=head.next
    while cur:
        print(cur.data)
        cur=cur.next

