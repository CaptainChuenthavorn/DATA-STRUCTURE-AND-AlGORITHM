def sumOfArray(arr,n):
    if n==len(arr)-1:
        return arr[n]
    else:
        return arr[n]+sumOfArray(arr,n+1)

#ลด จำนวนตัวหลัง
def summ(n,l):
    if n is 0:
        return 0
    elif n is 1:
        return l[0]
    else:
        return summ(n-1,l)+l[n-1]
#ลดจำนวนตัวหน้า ดึงออก
def sumF():
    pass
    
arr=[7,3,5,4,2,6,8,5,4,94,3,9,4,2,1]
print(sum(arr))
a= sumOfArray(arr,0)
print(a)
b= summ(len(arr),arr)
print(b)