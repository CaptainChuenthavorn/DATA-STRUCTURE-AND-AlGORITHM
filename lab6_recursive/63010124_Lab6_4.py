'''
 * กลุ่มที่  : 21010001
 * 63010124 จักรภัทรณ์ ชื่นถาวร
 * chapter : 6	item : 4	ครั้งที่ : 0002
 * Assigned : Thursday 16th of September 2021 11:26:34 AM --> Submission : Sunday 19th of September 2021 10:41:24 AM	
 * Elapsed time : 4274 minutes.
 * filename : 4.py
'''
'''
Enter Input (Money, Product) : 20/20 10 5 5 3 2 20 10
20
10 5 5
10 5 3 2
10 5 3 2
10 10
5 5 10
5 3 2 10
5 3 2 10
20
Krisada can purchase Product: [20, 10, 5, 5, 3, 2, 20, 10] with: 20 Baht | 9 Pattern
'''
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