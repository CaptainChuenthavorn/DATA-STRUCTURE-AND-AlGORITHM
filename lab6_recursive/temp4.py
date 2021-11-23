def store_count(count):
    count+=1 
    print('count',count)
    return count
glocount = 0
def pantip(k, n, arr, path,ans,count):
    t=len(ans)
    global glocount
    if n == len(arr)-1:
        if sum(path)==k:
            ans.append(path)
            print(*path)
            glocount+=1
        return 
    #start n+1 == start index 0
    path.append(arr[n+1])
    pantip(k,n+1,arr,path,ans,count)
    path.pop()
    #backtrack
    pantip(k,n+1,arr,path,ans,count)

inp = input('Enter Input (Money, Product) : ').split('/')
arr = [int(i) for i in inp[1].split()]
pattern = pantip(int(inp[0]), -1, arr, [],[],0)
print("Krisada can purchase Product: {0} with: {1} Baht | {2} Pattern".format(arr, inp[0], glocount))