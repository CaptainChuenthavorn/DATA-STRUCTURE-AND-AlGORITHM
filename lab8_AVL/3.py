class Node(object): 
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None
        self.height = 1
    def __str__(self):
        return str(self.val)
class AVL_Tree:
    def getHeight(self, root):
        if not root:
            return 0
        else:
            return root.height
    def getBalance(self, root):
        return self.getHeight(root.left) - self.getHeight(root.right)
    def insert(self, root, val):
        if not root:
            return Node(val)
        if val >= root.val:
            root.right = self.insert(root.right, val)
        else:
            root.left = self.insert(root.left, val)
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balance = self.getBalance(root)
        if balance > 1 and root.left.val >= val:
            print("Not Balance, Rebalance!")
            return self.rotateRight(root)
        if balance < -1 and root.right.val < val:
            print("Not Balance, Rebalance!")
            return self.rotateLeft(root)
        if balance < -1 and root.right.val > val:
            print("Not Balance, Rebalance!")
            root.right = self.rotateRight(root.right)
            return self.rotateLeft(root)
        if balance > 1 and root.left.val < val:
            print("Not Balance, Rebalance!")
            root.left = self.rotateLeft(root.left)
            return self.rotateRight(root)
        return root
    def rotateRight(self, z):
        y = z.left
        T3 = y.right
        z.left = T3
        y.right = z
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y
    def rotateLeft(self, z): 
        y = z.right
        T2 = y.left
        z.right = T2
        y.left = z
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y
def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)
myTree = AVL_Tree() 
root = None
data = input("Enter Input : ").split()
for e in data:
    print("insert :",e)
    root = myTree.insert(root, int(e))
    printTree90(root)
    print("===============")