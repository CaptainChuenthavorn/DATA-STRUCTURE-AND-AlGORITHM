'''
 * กลุ่มที่  : 21010001
 * 63010124 จักรภัทรณ์ ชื่นถาวร
 * chapter : 7	item : 4	ครั้งที่ : 0007
 * Assigned : Thursday 28th of October 2021 09:54:25 AM --> Submission : Friday 29th of October 2021 09:19:09 PM	
 * Elapsed time : 2124 minutes.
 * filename : 63010124_Lab6_4.py
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.level = None 

    def __str__(self):
        return str(self.data)

class BinarySearchTree:
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
    #time complexity 
    def delelte(self,root,key):
        if not root:
            return None
        #if data == root
        if root.data==key:
            #4 possiblities
            if not root.left and not root.right: 
                return None
            if not root.left and root.right:
                return root.right
            if root.left and not root.right:
                return root.left
            #if both have child
            #ให้หาเลขที่มาแทนก่อน แล้วก้เอาเลขมาแทนroot แล้วลบnodeเลขmin ออกไป
            pnt=root.right
            while pnt.left:
                pnt=pnt.left
            root.data = pnt.data
            root.right = self.delelte(root.right,root.data)
            
        #if root > data
        elif root.data>key:
            root.left = self.delelte(root.left,key)
        else:
            root.right = self.delelte(root.right,key)
        return root
    def searchNode(self,value):
        if self.root!=None:
            return self._searchNode(value,self.root)
        else:
            return False

    def _searchNode(self,value,cur_node):
        if value==cur_node.data:
            return True
        elif value<cur_node.data and cur_node.left!=None:
            return self._searchNode(value,cur_node.left)
        elif value>cur_node.data and cur_node.right!=None:
            return self._searchNode(value,cur_node.right)
        return False

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

tree = BinarySearchTree()
data = input("Enter Input : ").split(",")
#code here
for i in data:
    root=tree.root
    if i[0]=='i':
        tree.insert(int(i[2:]))
        root=tree.root
        print('insert',i[2:])
        printTree90(root)
    else:
        if root==None or not tree.searchNode(int(i[2:])):
            print('delete',i[2:])
            print('Error! Not Found DATA')
            printTree90(root)
        else:

            root = tree.delelte(root,int(i[2:]))
            tree.root=root
            print('delete',i[2:])
            printTree90(root)