#take half of each array is eliminated  with sorted array
#always round down when it left 2 we select index 0
#Advantage good for big data because it cut halfๆ bigO:logN
def interpolation(arr,value):
    low =0
    high = len(arr)-1
    while value >= arr[low] and value <= arr[high] and low<=high:
        probe = low+(high-low)*(value-arr[low]) // (arr[high]-arr[low])
        print('probe',probe)
        if arr[probe]==value:
            return probe
        elif arr[probe]<value:
            low=probe+1
        else:
            high=probe+1
    return -1

arr=[x for x in range(20)]
target=8
print(arr)
#for i in range(len(arr)):

index=interpolation(arr,target)

if index== -1:
    print('Element not found!')
else:
    print('Element found at index',index)
