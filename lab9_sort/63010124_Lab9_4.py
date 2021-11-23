def bub(lst,index,round,ans):
    if round == 0:
        print(*ans)
        return 
    else:
        #case next index is None
        if index == len(lst)-1:
            index=0
        
        if lst[index]>lst[index+1]:
            lst[index],lst[index+1]=lst[index+1],lst[index]
            ans[index],ans[index+1]=ans[index+1],ans[index]
        bub(lst,index+1,round-1,ans)

def calVol(data):
    ans=[]
    for i in data:
        if i not in '0123456789':
            ans.append(ord(i))
    return sum(ans)

inp= input('Enter Input : ').split()
ans=[]
for i in inp:
    a=calVol(i)
    ans.append(a)

bub(ans,0,len(ans)*len(ans),inp)