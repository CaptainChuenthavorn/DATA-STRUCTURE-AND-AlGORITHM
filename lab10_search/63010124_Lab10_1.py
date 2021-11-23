#l = low
#r = high
#x = target

def bi_search(l, r, arr, x):
    # Code Here
    if r>=l:
        middle = (r+l)//2
        value=arr[middle]
        
        if value==x:
            return True
        elif value>x:            
            return bi_search(l,middle-1,arr,x)
        else:
            return bi_search(middle+1,r,arr,x)
        
    else:
        return False
inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
print(bi_search(0, len(arr) - 1, sorted(arr), k))

#33 2 11 82 77 28 15 76 9 64/28