'''
 * กลุ่มที่  : 21010001
 * 63010124 จักรภัทรณ์ ชื่นถาวร
 * chapter : 7	item : 3	ครั้งที่ : 0001
 * Assigned : Wednesday 27th of October 2021 09:45:34 AM --> Submission : Friday 29th of October 2021 04:24:50 PM	
 * Elapsed time : 3279 minutes.
 * filename : 63010124_Lab6_3.py
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root ==None:
            self.root=Node(data)
        else:
            self._insert(data,self.root)

    def _insert(self,data,cur_node):
        if data < cur_node.data:
            if cur_node.left == None:
                cur_node.left=Node(data)
            else:
                self._insert(data,cur_node.left)
        elif data > cur_node.data:
            if cur_node.right == None:
                cur_node.right=Node(data)
            else:
                self._insert(data,cur_node.right)
    
    def findMax(self,node):
        if node.right==None:
            return node.data
        return self.findMax(node.right)
    
    def findMin(self,node):
        if node.left==None:
            return node.data
        return self.findMin(node.left)

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def inorderTraversalFindBelow(self,node,K):
        elements=[]
        if node.left!=None:
            #node left have item
            elements+=self.inorderTraversalFindBelow(node.left,K)
        if K>=node.data:
            elements.append(node.data)
        if node.right!=None:
            elements+=self.inorderTraversalFindBelow(node.right,K)
        return elements

T = BST()
inp = [str(i) for i in input('Enter Input : ').split('/')]
raw = [int(x) for x in inp[0].split()]
K=int(inp[1])
for i in raw:
    T.insert(int(i))
root=T.root
T.printTree(root)
print('--------------------------------------------------')
ele=T.inorderTraversalFindBelow(root,K)
print(len(ele))