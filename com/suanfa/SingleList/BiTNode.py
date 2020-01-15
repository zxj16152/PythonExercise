from collections import deque


class BiTNode:
    def __init__(self):
        self.data=None
        self.lchild=None
        self.rchild=None
def arrayToTree(arr,start,end):
    root=None
    if end>=start:
        root=BiTNode()
        mid=(start+end+1)//2
        root.data=arr[mid]
        root.lchild=arrayToTree(arr,start,mid-1)
        root.rchild=arrayToTree(arr,mid+1,end)
    else:
        root=None
    return root
def printTree(root):
    if not root:
        return
    if root.lchild:
        printTree(root.lchild)
    print(root.data,end=" ")
    if root.rchild:
        printTree(root.rchild)

def printTreeLayer(root):
    if not root:
        return
    queue=deque()
    queue.append(root)
    while queue:
        p = queue.popleft()
        print(p.data,end=" ")
        if p.lchild:
            queue.append(p.lchild)
        if p.rchild:
            queue.append(p.rchild)

def printTreeDFS(root):
    if not root:
        return
    stack=[]
    stack.append(root)
    while stack:
        p = stack.pop()
        print(p.data,end=" ")
        if p.rchild:
            stack.append(p.rchild)
        if p.lchild:
            stack.append(p.lchild)

def findMaxSubTree(root):  #子树的最大和
    maxSum=-2**32
    if not root:
        return 0
    lmax=findMaxSubTree(root.lchild)
    rmax=findMaxSubTree(root.rchild)
    sums=lmax+rmax+root.data
    if sums>maxSum:
        maxSum=sums;
    return maxSum
class Test:
    def __init__(self):
        self.pHead=None
        self.pEnd=None
    def convertTreeToList(self,root): #将二叉树变为双向链表
        if not root:
            return
        self.convertTreeToList(root.lchild)
        root.lchild=self.pEnd
        if not self.pEnd:
            self.pHead=root
        else:
            self.pEnd.rchild=root
            root.lchild=self.pEnd
        self.pEnd=root
        self.convertTreeToList(root.rchild)



pHead=None
pEnd=None
def convertTreeToList(root): #将二叉树变为双向链表
    global pHead,pEnd
    if not root:
        return
    convertTreeToList(root.lchild)
    root.lchild=pEnd
    if not pEnd:
        pHead=root
    else:
        pEnd.rchild=root
        root.lchild=pEnd
    pEnd=root
    convertTreeToList(root.rchild)
    return pHead





if __name__ == '__main__':
    arr=[1,2,3,4,5,6,7]
    # arr=[1,2,3]
    root=arrayToTree(arr,0,len(arr)-1)
    printTreeLayer(root)
    print("=="*25)
    # test=Test()
    # test.convertTreeToList(root)
    # cur=test.pHead
    head = convertTreeToList(root)
    cur=head
    while cur:
        print(cur.data)
        cur=cur.rchild


    # printTree(root)
    # print()
    # print("--"*25)
    # printTreeLayer(root)
    # print()
    # print("--"*25)
    # printTreeDFS(root)

    # arr=[4,2,5,6,1,3,6,8,2,3,-8]
    # root=arrayToTree(arr,0,len(arr)-1)
    # printTreeLayer(root)
    # print(findMaxSubTree(root))
