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
    def dele(self,root,key):
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
            root.right = self.dele(root.right,root.data)
            
        #if root > data
        elif root.data>key:
            root.left = self.dele(root.left,key)
        else:
            root.right = self.dele(root.right,key)
        return root

    def delelte(self,r,data):
        if r is None:
            return r
        if data<r.data:
            r.left=self.delelte(r.left,data)
        elif data>r.data:
            r.right=self.delelte(r.right,data)
        #data == root.value
        else:
            #one child or no child
            if r.left is None:
                temp = r.right
                r = None
                return temp
            elif r.right is None:
                temp=r.left
                r = None
                return temp
            #node with two child
            #get inorder successor
            temp = self.minValueNode(r.right)
            #copy inorder successor to this node
            r.data =temp.data
            #delete the inorder succesor
            r.right = self.delelte(r.right,temp.data)
        return root


    def getSuccessorInorder(self,node):
        if node.right is not None:
            return self.minValue(node.right)
        succ =Node(None)
        while(self.root):
            if self.root.data<node.data:
                self.root=self.root.right
            elif self.root.data>node.data:
                succ=self.root
                self.root=self.root.left
            else:
                break
        return succ

    def searchNode(self,value):
        if self.root!=None:
            return self._searchNode(value,self.root)
        else:
            return False

    def _searchNode(self,value,cur_node):
        if value==cur_node.data:
            return cur_node
        elif value<cur_node.data and cur_node.left!=None:
            return self._searchNode(value,cur_node.left)
        elif value>cur_node.data and cur_node.right!=None:
            return self._searchNode(value,cur_node.right)
        return False

    def minValueNode(node):
        current = node
    
        # loop down to find the leftmost leaf
        while(current.left is not None):
            current = current.left
    
        return current
    def minValue(self,node):
        current=node
        while current is not None:
            if current.left is None:
                break
            current = current.left

        return current

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

tree = BinarySearchTree()
'''data = input("Enter Input : ").split(",")
#code here
for i in data:
    if i[0]=='i':
        tree.insert(int(i[1:]))
    else:
        tree.delelte()'''
raw=[20,8,22,4,12,10,14]
raw=[3,5,2]
raw=[0,2,1,4,5,3]
for i in raw:
    tree.insert(int(i))
root=tree.root
printTree90(root)
print('--------------------------------------------------')
print('delete 20')
r=tree.dele(root,2)
printTree90(root)
#nodeD=tree.searchNode(temp)
#succ=tree.getSuccessorInorder(nodeD)
#if succ is not None:
#    print("Inorder Successor of" ,temp ,"is" ,succ.data)
#else:
#    print("InInorder Successor doesn't exist")
