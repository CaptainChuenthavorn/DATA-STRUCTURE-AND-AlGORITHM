'''
 * กลุ่มที่  : 21010001
 * 63010124 จักรภัทรณ์ ชื่นถาวร
 * chapter : 7	item : 1	ครั้งที่ : 0001
 * Assigned : Tuesday 26th of October 2021 12:01:30 PM --> Submission : Thursday 28th of October 2021 02:12:56 PM	
 * Elapsed time : 3011 minutes.
 * filename : 63010124_Lab6_1.py
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
            if cur_node.left != None:
                self._insert(data,cur_node.left)
            else:
                cur_node.left=Node(data)
        elif data > cur_node.data:
            if cur_node.right != None:
                self._insert(data,cur_node.right)
            else:
                cur_node.right=Node(data)
        else:
            print('duplicate',data)

    def printTree(self, node, level = 0):
        
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    T.insert(i)
root=T.root
T.printTree(root)