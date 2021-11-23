'''power: 5 4 4 3 2 2 2
index: 0 1 2 3 4 5 6
n , 2n+1 ,2n+2
group 0 : 0 , 1 , 2 
          5   4   4 = 13 
group 1 : 1 , 3 , 5  
          4   3   2 = 13
group 2 : 2 , 5 , 6  
          4   2   2 = 8
group 3 : 3 , 7 , 8  
          3   0   0 = 3
group 4 : 4 , 9 , 10 
          2   0   0 =  2
group 5 : 5 , 11 , 12 
          2   0   0 = 2
group 6 : 6 , 13 , 14
          2   0   0 = 2
สร้าง tree ของแต่ละลำดับแล้วsum เอาผลลัพธ์ที่sumมาcompare
'''

class Node:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right
    
#class AVLBST():
    '''def insert(root,data):
        if root==None:
            root=Node(data)
        else:
            if data>=root.data:
                if root.right ==None:
                    print('we get in ')
                    root.right = Node(data)
                else:
                    insert(root.right,data)
            elif data<root.data:
                if root.left ==None:
                    root.left = Node(data)
                else:
                    insert(root.left,data)
    '''
def insert(root, data):
    if root ==None:
        root=Node(data)
    else:
        return _insert(data,root)
    return root
def _insert(data,cur_node):
    if data < cur_node.data:
        if cur_node.left != None:
            _insert(data,cur_node.left)
        else:
            cur_node.left=Node(data)
    elif data >= cur_node.data:
        if cur_node.right != None:
            _insert(data,cur_node.right)
        else:
            cur_node.right=Node(data)
    return cur_node
def sums(node):
    if node is None:
        return 0
    return node.data + sums(node.left) + sums(node.right)

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node.data)
        printTree90(node.left, level + 1)

def buildSerial(nlen,data):
    pass
inp = input("Enter Input : ").split('/')
power = [int(x) for x in inp[0].split()]
order = [str(x) for x in inp[1].split(',')]
print(sum(power))
for i in order:
    n1 = int(i[:1])
    n2 = int(i[2:])
    lst1=[]
    lst2=[]
    if n1 <len(power):
        lst1.append(power[n1])
    if (n1*2)+1 < len(power):
        lst1.append(power[(n1*2)+1])
    if (n1*2)+2 < len(power):
        lst1.append(power[(n1*2)+2])
    #n2
    if n2 <len(power):
        lst2.append(power[n2])
    if (n2*2)+1 < len(power):
        lst2.append(power[(n2*2)+1])
    if (n2*2)+2 < len(power):
        lst2.append(power[(n2*2)+2])
    rootA=None
    rootB=None
    for x in lst1:
        rootA = insert(rootA,x)
    for x in lst2:
        rootB = insert(rootB,x)
    ans1=sums(rootA)
    ans2=sums(rootB)
    if ans1>ans2:
        print(f'{n1}>{n2}')
    elif ans1<ans2:
        print(f'{n1}<{n2}')
    elif ans1==ans2:
        print(f'{n1}={n2}')