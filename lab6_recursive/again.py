def pantip(k, n, arr, path,len):
    if len == 0:
        if sum(path)==k:
            path.reverse()
            print(path)
        return 
    path.append(arr[len-1])
    pantip(k,n,arr,path,len-1)
    path.pop()
    #backtrack
    pantip(k,n,arr,path,len-1)
inp = input('Enter Input (Money, Product) : ').split('/')
arr = [int(i) for i in inp[1].split()]
len = len(arr)
pattern = pantip(int(inp[0]), 0, arr, [],len)
print("Krisada can purchase Product: {0} with: {1} Baht | {2} Pattern".format(arr, inp[0], pattern))