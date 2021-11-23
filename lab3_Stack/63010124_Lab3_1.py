'''
 * กลุ่มที่  : 21010001
 * 63010124 จักรภัทรณ์ ชื่นถาวร
 * chapter : 3	item : 1	ครั้งที่ : 0001
 * Assigned : Wednesday 1st of September 2021 10:09:04 AM --> Submission : Wednesday 1st of September 2021 10:15:37 AM	
 * Elapsed time : 6 minutes.
 * filename : 63010124_Lab3_1.py
'''
class Stack():
    def __init__(self,i=None):
        if i==None:
            self.items=[]
        else:
            self.items=i
    def push(self,i):
        self.items.append(i)
    def pop(self):
        self.items.pop()
    def isEmpty(self):
        return len(self.items)==0
    def size(self):
        return len(self.items)
    
print(" *** Stack implement by Python list***")

ls = [e for e in input("Enter data to stack : ").split()]

s = Stack()

for e in ls:

    s.push(e)

print(s.size(),"Data in stack : ",s.items)

while not s.isEmpty():

    s.pop()

print(s.size(),"Data in stack : ",s.items)