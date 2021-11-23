'''
 * กลุ่มที่  : 21010001
 * 63010124 จักรภัทรณ์ ชื่นถาวร
 * chapter : 8	item : 3	ครั้งที่ : 0001
 * Assigned : Wednesday 27th of October 2021 09:45:40 AM --> Submission : Wednesday 10th of November 2021 10:34:32 AM	
 * Elapsed time : 20208 minutes.
 * filename : 63010124_Lab8_3.py
'''
def traverse(tree, index = 0):
    if tree[index] is not None:
        return tree[index]
    l = traverse(tree, 2*index+1)
    r = traverse(tree, 2*index+2)
    if l < r:
        tree[index] = tree[2*index+1]
        tree[2*index+2] -= tree[2*index+1]
        tree[2*index+1] = 0
    else:
        tree[index] = tree[2*index+2]
        tree[2*index+1] -= tree[2*index+2]
        tree[2*index+2] = 0
    return tree[index]

def sums(tree,index = 0):
    if index > len(tree) -1:
        return 0
    if tree[index] is None:
        return 0
    return tree[index] + sums(tree, 2*index+1) + sums(tree, 2*index+2)


def printTree(tree, level = 0, index = 0):
    if index > len(tree)-1:
        return
    if tree[index] is not None:
        printTree(tree, level + 1,2*index+2)
        print('     '*level, tree[index])
        printTree(tree, level + 1, 2*index+1)

n, l =  input("Enter Input : ").split('/')
l = list(map(int, l.split()))
#กันเคส [N / 2] + 1
if len(l) != int(n)//2+1:
    print("Incorrect Input")
else:
    tree = [None]*int(n)
    for i in range(int(n)//2, int(n)):
        tree[i] = l[i - int(n)//2]
    traverse(tree)
    print(sums(tree))