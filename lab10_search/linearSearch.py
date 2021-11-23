
def linearSearch(arr,value):
    for i in range(len(arr)):
        if arr[i]==value:
            return i
    return -1

arr =[9,1,8,2,7,6,3,4,5]
index = linearSearch(arr,2)
if index== -1:
    print('Element not found!')
else:
    print('Element found at index',index)
