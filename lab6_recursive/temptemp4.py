#20/20 10 5 5 3 2 20 10

def pantip(k, n, arr, path,count,ans):
    print(n,ans)
    if count>30:
        return len(ans) 
    if n==len(arr)-1:
        n=0        
        return pantip(k,n,arr,path,count,ans)
    if arr[n] + sum(path) <=k:
        path.append(arr[n])
        return pantip(k,n,arr,path,count,ans)
    if sum(path)==k:
        if path in ans:
            count+=1
            return pantip(k,n+1,arr,path,count,ans)
        else:
            print('path:',*path,'n:',n,'all index',len(arr))
            ans.append(path)
            path.clear()
            count=0
            return pantip(k,n,arr,path,count,ans)
    
    
    else:
        return pantip(k,n+1,arr,path,count,ans)

inp = input('Enter Input (Money, Product) : ').split('/')
arr = [int(i) for i in inp[1].split()]
count=0
pattern = pantip(int(inp[0]), 0, arr, [],count,[])
print("Krisada can purchase Product: {0} with: {1} Baht | {2} Pattern".format(arr, inp[0], pattern))