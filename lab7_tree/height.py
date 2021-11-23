class Node:
    def __init__(self,value):
        self.value=value
        #self.left=None if left is None else left
        #self.right=None if right is None else right
        self.left = None
        self.right = None
    def __str__(self):
        return self.value
class Bst():
    def __init__(self):
        self.root=None
    def insert(self,data):
        if self.root==None:
            self.root=Node(data)
        else:
            self._insert(self.root,data)

    def _insert(self,node,data):
        if data > node.value:
            if node.right==None:
                #if node right is empty add!
                node.right = Node(data)
            else:
                self._insert(node.right,data)
        elif data < node.value:
            if node.left==None:
                #if node right is empty add!
                node.left = Node(data)
            else:
                self._insert(node.left,data)
    def printTree(self, node, level = 0):
        
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node.value)
            self.printTree(node.left, level + 1)
                
    def height(self):
        if self.root==None:
            return 0
        else:
            return self._height(self.root)
    def _height(self,node):
        if node is None:
            return -1
        else:
            return 1+max(self._height(node.left),self._height(node.right))

T=Bst()
s=[3,5,2,1,4,6,7]
for i in s:
    T.insert(i)
root=T.root
T.printTree(root)
a=T.height()
print('height : ',a)