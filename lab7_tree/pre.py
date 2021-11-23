class Node():
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
    def __str__(self):
        return str(self.data)

class BST():
    def __init__(self):
        self.root=None
    
    def insert(self,data):
        if self.root==None:
            self.root=Node(data)
        else:
            return self._insert(self.root,data)
    
    def _insert(self,root,data):
        if data<root.data:
            #if left none child
            if root.left==None:
                root.left =Node(data)
            else:
                return self._insert(root.left,data)
        if data>root.data:
            #if right none child
            if root.right==None:
                root.right =Node(data)
            else:
                return self._insert(root.right,data)
    def inorderTraversal(self,node):
        elements=[]
        if node.left!=None:
            elements+=self.inorderTraversal(node.left)
        elements.append(node.data)
        if node.right!=None:
            elements+=self.inorderTraversal(node.right)
        return elements
    
    def search(self,data):
        if self.root ==None:
            return False
        else self._search

def printTree(node,level=0):
    if node!=None:
        printTree(node.right,level+1)
        print('     '*level,node)
        printTree(node.left,level+1)

T=BST()
n=['A','C','B','D']
for i in n:
    T.insert(i)
printTree(T.root)

a=T.inorderTraversal(T.root)
print(a)