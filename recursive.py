'''
เป็นการ backtrack 
วิธีสร้าง 1.ต้องมีพารามิเตอร์
2.recursive call โดยเปลี่ยน parameter
3.ต้องมี base case / simple case
'''
def Fac(n):
    #n>=0
    Fac(n-1)*n
def EatUp(n):
    if n>1: 
        EatUp(n-1)
        print('eat1')
    #n<=1
    elif n==1: #base case
        print('eatq')
    #base case : n<=0: do nothing
def binarySearch(low,high,x):
    if high< low:
        return -1
    mid = (low+high)/2
    if x==a[mid]:
        return mid
    elif a[mid]<x:
        return binarySearch(mid+1,high,x)#recursive
    else:
        return binarySearch(low,mid-1,x)
#EatUp(8)