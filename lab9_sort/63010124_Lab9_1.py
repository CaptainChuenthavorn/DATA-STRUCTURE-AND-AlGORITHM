
def bub(lst,index,round):
    if round == 0:
        #print(lst)
        return lst
    else:
        #case next index is None
        if index == len(lst)-1:
            index=0
        
        if lst[index]>lst[index+1]:
            lst[index],lst[index+1]=lst[index+1],lst[index]
        return bub(lst,index+1,round-1)
'''
ส่งlst กับ index ตรวจindex maxก่อน ,round (len(lst)-1)
'''

if __name__ == '__main__':

    A = [int(x) for x in input("Enter Input : ").split()]
    print(bub(A,0,len(A)*len(A)))
    