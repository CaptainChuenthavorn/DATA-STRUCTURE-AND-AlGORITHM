'''
 * กลุ่มที่  : 21010001
 * 63010124 จักรภัทรณ์ ชื่นถาวร
 * chapter : 8	item : 2	ครั้งที่ : 0005
 * Assigned : Saturday 30th of October 2021 10:02:06 AM --> Submission : Monday 8th of November 2021 02:00:35 PM	
 * Elapsed time : 13198 minutes.
 * filename : AVLComplete.py
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1   
    
    def __str__(self):
        return str(self.data)

class AVL:


    def insert(self,data,cur_node):
        if cur_node == None:
            return Node(data)
        elif cur_node.data>data:
            cur_node.left = self.insert(data,cur_node.left)
        elif cur_node.data<=data:
            cur_node.right = self.insert(data,cur_node.right)
        #updata height of ancestor(grandparent)
        cur_node.height=1+max(self.get_height(cur_node.left),self.get_height(cur_node.right))
        #get balance facter
        balance = self.get_balance(cur_node)
        #if node is unbalance we have 4 case support
        #left left
        '''if balance > 1 and data < cur_node.left.data:
            return self.rightRotate(cur_node)
        #right right
        if balance < -1 and data > cur_node.right.data:
            return self.leftRotate(cur_node)
        #left right
        if balance > 1 and data > cur_node.left.data:
            cur_node.left = self.leftRotate(cur_node.left)
            return self.rightRotate(root)
        #right left
        if balance <-1 and data < root.right.val:
            cur_node.right = self.rightRotate(cur_node.right)
            return self.leftRotate(cur_node)
        
        '''
        if balance > 1 and data < cur_node.left.data:
            return self.rightRotate(cur_node)
        if balance > 1 and data >= cur_node.left.data:
            cur_node.left = self.leftRotate(cur_node.left)
            return self.rightRotate(cur_node)
        if balance < -1 and data >= cur_node.right.data:
            return self.leftRotate(cur_node)
        if balance < -1 and data < cur_node.right.data:
            cur_node.right = self.rightRotate(cur_node.right)
            return self.leftRotate(cur_node)
        return cur_node

    def leftRotate(self,node):
        y=node.right
        x=y.left
        #Perform ratation
        y.left = node 
        node.right = x
        #update height
        node.height = 1+max(self.get_height(node.left),self.get_height(node.right))
        y.height = 1+max(self.get_height(y.left),self.get_height(y.right))
        #return new root
        return y
    def rightRotate(self,node):
        y=node.left
        x=y.right
        #Perform ratation
        y.right = node 
        node.left = x
        #update height
        node.height = 1+max(self.get_height(node.left),self.get_height(node.right))
        y.height = 1+max(self.get_height(y.left),self.get_height(y.right))
        #return new root
        return y
    
    def get_height(self,node):
        if node is None:
            return 0
        return node.height

    def get_balance(self, node):
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def printTree(self,node,level=0):
        if node!=None:
            self.printTree(node.right,level+1)
            print('     '*level,node)
            self.printTree(node.left,level+1)

if __name__ == '__main__':
    T = AVL()
    inp = [int(i) for i in input('Enter Input : ').split()]
    root =None
    for i in inp:
        print(f'Insert : ( {i} )')
        root = T.insert(i,root)
        T.printTree(root)
        print('--------------------------------------------------')