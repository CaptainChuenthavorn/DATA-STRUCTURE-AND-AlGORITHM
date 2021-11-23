'''
 * กลุ่มที่  : 21010001
 * 63010124 จักรภัทรณ์ ชื่นถาวร
 * chapter : 3	item : 3	ครั้งที่ : 0002
 * Assigned : Wednesday 1st of September 2021 11:08:07 AM --> Submission : Wednesday 1st of September 2021 11:20:45 AM	
 * Elapsed time : 12 minutes.
 * filename : 63010124_Lab3_3.py
'''
class Stack():
    def __init__(self,i=None):
        if i==None:
            self.items=[]
        else:
            self.items=i
    def push(self,i):
        self.items.append(i)
    def pop(self,i):
        return self.items.pop(i)
    def isEmpty(self):
        return len(self.items)==0
    def size(self):
        return len(self.items)

inp = input('Enter Input : ').split()
S = Stack()
combo=0
for i in inp:
    S.push(i)
    n = S.items.index(i)
    if S.items.count(i)==3:
        S.pop(n)
        S.pop(n)
        S.pop(n)
        combo+=1
print(S.size())
if S.size()==0:
    print('Empty')
else :
    print(''.join(S.items[::-1]))
if combo>1:
    print('Combo :',combo,'! ! !')
