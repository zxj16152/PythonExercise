class Node:
    def __init__(self,data=None):
        self.left=None
        self.right=None
        self.data=data


class BinarySearchTree:
    def __init__(self,root=None):
        self.root=root

    def add(self,data):
        node = Node(data)
        if not self.root:
            self.root=node
        else:
            queue=[]
            queue.append(self.root)
            while queue:
                cur = queue.pop(0)
                if not cur.left:
                    cur.left=node
                    return
                elif not cur.right:
                    cur.right=node
                    return
                else:
                    queue.append(cur.left)
                    queue.append(cur.right)
    def frontTravel(self,root):
        if  root:
            print(root.data)
            self.frontTravel(root.left)
            self.frontTravel(root.right)

    def breathTravel(self,root):
        queue=[]
        if root:
            queue.append(root)
            count=0
            pricoun=1
            while queue:
                cur = queue.pop(0)
                count+=1
                print(cur.data,end=" ")
                if count==2**pricoun-1:
                    print("")
                    pricoun+=1
                if not cur.left:
                    continue
                elif not cur.right:
                    continue
                else:
                    # print(cur.left.data)
                    # print(cur.right.data)
                    queue.append(cur.left)
                    queue.append(cur.right)
                # print()


    # def find(self,data):
    #     cur=self.head
    #     while cur:
    #         if data<cur.data:
    #             cur=cur.left
    #         elif data>cur.data:
    #             cur=cur.right
    #         else:
    #             return cur
    # def insert(self,data):
    #     node=Node(data)
    #     cur=self.head
    #     if not cur:
    #         cur=node
    #         return
    #     while cur:
    #         if data>cur.data:
    #             if not cur.right:
    #                 cur.right=node
    #                 return
    #             else:
    #                 cur=cur.right
    #         else:
    #             if not cur.left:
    #                 cur.left=node
    #                 return
    #             cur=cur.left
    # def frontTravel(self,node):
    #     cur=self.head
    #     if not cur :
    #         return
    #     print(cur.data)
    #     if cur.left:
    #         self.frontTravel(cur.left)
    #         # print(self.left.data)
    #     if cur.right:
    #         self.frontTravel(cur.right)
    #         # print(self.right.data)
    #
    # def midTravel(self):
    #     cur=self.head
    #     if not cur:
    #         return
    #     if cur.left:
    #         cur.left.midTravel()
    #     print(cur.data)
    #     if cur.right:
    #         cur.right.midTravel()

                



        
if __name__ == '__main__':

    tree = BinarySearchTree(Node('A'))
    tree.add('B')
    tree.add('C')
    tree.add('D')
    tree.add('E')
    tree.add('F')
    tree.add('G')
    # tree.add(8)
    # tree.frontTravel(tree.root)
    tree.breathTravel(tree.root)