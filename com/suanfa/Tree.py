class TreeNode:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.item = item

    def frontTravel(self):
        if not self :
            return
        print(self.item)
        if self.left:
            self.left.frontTravel()
            # print(self.left.item)
        if self.right:
            self.right.frontTravel()
            # print(self.right.item)

    def midTravel(self):
        if not self:
            return
        if self.left:
            self.left.midTravel()
        print(self.item)
        if self.right:
            self.right.midTravel()



a = TreeNode('A')
b = TreeNode('B')
c = TreeNode('C')
d = TreeNode('D')
e = TreeNode('E')
f = TreeNode('F')
g = TreeNode('G')
a.left=b
a.right=c
b.left=d
b.right=e
c.left=f
c.right=g
# a.frontTravel()
a.midTravel()