'''
น้อย ไป มาก ไม่ซ้ำ Metadrome
น้อย ไป มาก ซ้ำ Plaindrome
มาก ไป น้อย ไม่ซ้ำ Katadrome
มาก ไป น้อย ซ้ำ Nialpdrome
เลขเดียวกันหมด Repdrome
ไม่อญู่ในเงื่อนไขด้านบน  Nondrome
'''

def checkMinToMax(lst):
    for i in range(len(lst)-1):
        if lst[i]>lst[i+1]:
            return False
    return True
def checkDuplicate(lst):
    s= set(lst)
    return not len(s) == len(lst)
def checkMaxtoMin(lst):
    for i in range(len(lst)-1):
        if lst[i]<lst[i+1]:
            return False
    return True
def checkAllnumSame(lst):
    numSame = True
    for i in range(len(lst)-1):
        if lst[i]!=lst[i+1]:
            numSame=False
    return numSame
inp=input("Enter Input : ")
lst=[]
for i in inp:
    lst.append(int(i))
s=set(lst)
if len(s)==1:
    print('Repdrome')
elif checkMinToMax(lst) and not checkDuplicate(lst):
    print('Metadrome')
elif checkMinToMax(lst) and checkDuplicate(lst):
    print('Plaindrome')
elif checkMaxtoMin(lst) and not checkDuplicate(lst):
    print('Katadrome')
elif checkMaxtoMin(lst) and checkDuplicate(lst):
    print('Nialpdrome')
else:
    print('Nondrome')