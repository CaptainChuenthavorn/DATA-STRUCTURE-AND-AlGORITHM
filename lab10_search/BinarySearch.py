#take half of each array is eliminated  with sorted array
#always round down when it left 2 we select index 0
#Advantage good for big data because it cut halfๆ bigO:logN
def binarySearch(arr,target):
    low =0
    high = len(arr)-1
    while low<=high:
        middle = low +(high-low)//2
        value=arr[middle]
        print('middle:',value)
        if value < target:
            low = middle+1
        elif value > target:
            high = middle-1
        else:
            return middle
    return -1

arr=[33,2, 11, 82, 77, 28, 15, 76, 9 ,64]
arr.sort()
target=28
print(arr)
#for i in range(len(arr)):

index=binarySearch(arr,target)

if index== -1:
    print('Element not found!')
else:
    print('Element found at index',index)
