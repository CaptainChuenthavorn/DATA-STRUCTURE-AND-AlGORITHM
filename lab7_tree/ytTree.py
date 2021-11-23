class BinarySearchTree():
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None
    def insert(self,data):
        if data == self.data:
            return #node already exist
        if data < self.data:
            if self.left:
                #if left have data already 
                self.left.insert(data)
            else:
                #if left is empty
                self.left = BinarySearchTree(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = BinarySearchTree(data)

    def search(self,val):
        if val==self.data:
            return True
        if val<self.data:
            #go left
            if self.left:
                #left is have data
                self.left.search(val)
            else:
                return False
        if val>self.data:
            #go right
            if self.right:
                self.right.search(val)
            else:
                return False
    def inorderTraversal(self):
        elements=[]
        if self.left:
            #if left have data
            elements+=self.left.inorderTraversal()
        elements.append(self.data)
        if self.right:
            elements+=self.right.inorderTraversal()
        return elements
    def preorderTraversal(self):
        elements=[self.data]
        #elements.append(self.data)
        if self.left:
            #if left have data
            elements+=self.left.preorderTraversal()
        if self.right:
            elements+=self.right.preorderTraversal()
        return elements
    def postorderTraversal(self):
        elements=[]
        
        if self.left:
            #if left have data
            elements+=self.left.postorderTraversal()
        if self.right:
            elements+=self.right.postorderTraversal()
        elements.append(self.data)
        return elements
    def findMin(self):
        if self.left==None:
            return self.data
        return self.left.findMin()
    def findMax(self):
        if self.right==None:
            return self.data
        return self.right.findMin()
def build_tree(elements):
    print('building a Binary Search Tree with these : ',elements)
    root = BinarySearchTree(elements[0])
    for i in range(1,len(elements)):
        root.insert(elements[i])
    return root
if __name__== '__main__':
    
    num = [15,12,27,7,14,20,88,23]
    num2=[30,40,10,50,20,5,35]
    T=build_tree(num)
    num2=[30,40,10,50,20,5,35]
    numbers_tree = build_tree(num2)
    ele1=T.inorderTraversal()
    print('Tree inorder Traversal :',ele1)
    ele2=T.preorderTraversal()
    print('Tree preorder Traversal :',ele2)
    ele3=T.postorderTraversal()
    print('Tree postorder Traversal :',ele3)
    min = T.findMin()
    print('Min :',min)
    max = T.findMax()
    print('Max :',max)