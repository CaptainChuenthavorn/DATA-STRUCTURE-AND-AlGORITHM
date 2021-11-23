def sum(n):
    if n==0:
        return 0
    else:
        return n+sum(n-1)
def path(n,m):
    if n==1 or m ==1:
        return 1
    else:
        return path(n,m-1)+path(n-1,m)
    
def partition(n,m):
    #simple input
    if n==0:
        return 1
    if m==0:
        return 0
    else:
        return (n-m)+partition(n,m-1) 

def hanoi(n,a,c,b):
    if n ==1:
        print(n,'form',a,'to',c)
    else:
        hanoi(n-1,a,b,c)
        print(n,'form',a,'to',c)
        hanoi(n-1,b,c,a)
a=hanoi(4,'a','b','c')
print('ans:',a)