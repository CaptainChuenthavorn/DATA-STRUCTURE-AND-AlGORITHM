'''
 * กลุ่มที่  : 21010001
 * 63010124 จักรภัทรณ์ ชื่นถาวร
 * chapter : 8	item : 5	ครั้งที่ : 0003
 * Assigned : Saturday 6th of November 2021 10:27:26 PM --> Submission : Monday 8th of November 2021 12:14:35 PM	
 * Elapsed time : 2267 minutes.
 * filename : 63010124_Lab8_5.py
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.data)

class Tree:
    def __init__(self):
        self.root = None
        self.num = 0

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
            self.num += 1
        else:
            h = height(self.root)
            max_node = pow(2, h + 1) - 1
            current = self.root
            if self.num + 1 > max_node:
                while current.left is not None:
                    current = current.left
                current.left = Node(val)
                self.num += 1
            elif self.num + 1 == max_node:
                while current.right is not None:
                    current = current.right
                current.right = Node(val)
                self.num += 1
            else:
                # print(max_node - ((max_node - (pow(2, h) - 1)) / 2))
                if self.num + 1 <= max_node - ((max_node - (pow(2, h) - 1)) / 2):
                    insert_subtree(current.left, self.num - round(pow(2, h) / 2), val)
                else:
                    insert_subtree(current.right, self.num - pow(2, h), val)
                self.num += 1


def insert_subtree(max, num, val):
    if max is not None:
        h = height(max)
        max_node = pow(2, h + 1) - 1
        current = max
        if num + 1 > max_node:
            while current.left is not None:
                current = current.left
            current.left = Node(val)
            return
        elif num + 1 == max_node:
            while current.right is not None:
                current = current.right
            current.right = Node(val)
            return
        if num + 1 <= max_node - ((max_node - (pow(2, h) - 1)) / 2):
            insert_subtree(current.left, num - round(pow(2, h) / 2), val)
        else:
            insert_subtree(current.right, num - pow(2, h), val)
    else:
        return


def height(root):
    if root is None:
        return -1
    else:
        left = height(root.left)
        right = height(root.right)
        if left > right:
            return left + 1
        else:
            return right + 1

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)


def check_binary_search_tree_(root, min = 0,max = 100):
    #code here
    if root is None:
        return True
    if root.data < min or root.data > max:
        return False
    return check_binary_search_tree_(root.left, min, root.data - 1) and check_binary_search_tree_(root.right, root.data + 1, max)

tree = Tree()
data = input("Enter Input : ").split()
for e in data:
    tree.insert(int(e))
printTree90(tree.root)
print(check_binary_search_tree_(tree.root))