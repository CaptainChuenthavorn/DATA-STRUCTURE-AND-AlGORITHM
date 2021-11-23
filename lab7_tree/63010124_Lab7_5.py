'''
 * กลุ่มที่  : 21010001
 * 63010124 จักรภัทรณ์ ชื่นถาวร
 * chapter : 7	item : 5	ครั้งที่ : 0001
 * Assigned : Friday 29th of October 2021 09:19:17 PM --> Submission : Saturday 30th of October 2021 07:02:37 PM	
 * Elapsed time : 1303 minutes.
 * filename : 63010124_Lab6_5.py
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

    def postfixToinfix(self,postfix):
        stack=[]
        for char in postfix:
            if not isOperator(char):
                t=Node(char)
                stack.append(t)
            else:
                t=Node(char)
                t1 = stack.pop()
                t2 = stack.pop()
                
                # make them children
                t.right = t1
                t.left = t2
                
                # Add this subexpression to stack
                stack.append(t)
    
        # Only element  will be the root of expression tree
        t = stack.pop()
        
        return t

    def inorderTraversal(self,node):
        elements=[]
        if node.left!=None:
            #node left have item
            elements.append('(')
            elements+=self.inorderTraversal(node.left)       
        
        
        elements.append(node.data)
        
        if node.right!=None:
            
            elements+=self.inorderTraversal(node.right)
            elements.append(')')
        return elements

    def preorderTraversal(self,node):
        elements=[]
        elements.append(node.data)
        if node.left!=None:
            #node left have item
            elements+=self.preorderTraversal(node.left)       
        if node.right!=None:
            elements+=self.preorderTraversal(node.right)
        return elements
    
    def preorderTraversal(self,node):
        elements=[]
        
        if node.left!=None:
            #node left have item
            elements+=self.preorderTraversal(node.left)       
        if node.right!=None:
            elements+=self.preorderTraversal(node.right)
        elements.append(node.data)
        return elements

def isOperator(c):
    if (c == '+' or c == '-' or c == '*' or c == '/' or c == '^'):
        return True
    else:
        return False
def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

tree = BinarySearchTree()
data = input("Enter Postfix : ")
print('Tree :')
#code here
root=tree.postfixToinfix(data)
printTree90(root)
infix = tree.inorderTraversal(root)
prefix = tree.preorderTraversal(root)
postfix = tree.postfixToinfix(root)
print('--------------------------------------------------')
print('Infix :',''.join(infix))
print('Prefix :',''.join(prefix))
print('Postfix :',''.join(postfix))

