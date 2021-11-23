'''
หอคอยแห่งฮานอย

Enter Input : 3
|  |  |
1  |  |
2  |  |
3  |  |
move 1 from  A to C
|  |  |
|  |  |
2  |  |
3  |  1
move 2 from  A to B
|  |  |
|  |  |
|  |  |
3  2  1
move 1 from  C to B
|  |  |
|  |  |
|  1  |
3  2  |
move 3 from  A to C
|  |  |
|  |  |
|  1  |
|  2  3
move 1 from  B to A
|  |  |
|  |  |
|  |  |
1  2  3
move 2 from  B to C
|  |  |
|  |  |
|  |  2
1  |  3
move 1 from  A to C
|  |  |
|  |  1
|  |  2
|  |  3

'''

A = []
B = []
C = []

def popPush(start, dest):
    global A
    global B
    global C

    if start == 'A':
        x = A.pop(0)
    elif start == 'B':
        x = B.pop(0)
    else:
        x = C.pop(0)

    if dest == 'A':
        A.insert(0, x)
    elif dest == 'B':
        B.insert(0, x)
    else:
        C.insert(0, x)

def printTower(maxn, row):
    global A
    global B
    global C
    a = A[::-1]
    b = B[::-1]
    c = C[::-1]

    if row == 0:
        return

    if row == maxn:
        print('|  |  |')

    if len(A) >= row:
        print(f"{a[row-1]}  ", end="")
    else:
        print('|  ', end="")

    if len(B) >= row:
        print(f"{b[row-1]}  ", end="")
    else:
        print('|  ', end="")

    if len(C) >= row:
        print(f"{c[row-1]}", end="")
    else:
        print('|', end="")
        
    if row != 0:
        print()
    printTower(maxn, row-1)

def move(n, A, B, C, maxn):
    if n == 1:
        print(f"move {n} from  {A} to {C}")
        popPush(A, C)
        printTower(maxn, maxn)
    else:
        move(n-1, A, C, B, maxn)
        print(f"move {n} from  {A} to {C}")
        popPush(A, C)
        printTower(maxn, maxn)
        move(n-1, B, A, C, maxn)

def recA(num, target):
    global A
    if num <= target:
        A.append(num)
        recA(num+1, target)

n = int(input("Enter Input : "))
recA(1, n)
printTower(n, n)
move(n, 'A', 'B', 'C', n)