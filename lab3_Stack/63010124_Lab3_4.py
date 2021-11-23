'''
 * กลุ่มที่  : 21010001
 * 63010124 จักรภัทรณ์ ชื่นถาวร
 * chapter : 3	item : 4	ครั้งที่ : 0001
 * Assigned : Wednesday 1st of September 2021 11:21:04 AM --> Submission : Thursday 2nd of September 2021 04:41:49 PM	
 * Elapsed time : 1760 minutes.
 * filename : 63010124_Lab3_4.py
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
        return self.items.pop()
    def isEmpty(self):
        return len(self.items)==0
    def size(self):
        return len(self.items)
    def peek(self):
        return self.items[len(self.items)-1]

def infix2postfix(exp) :

    s = Stack()
    str=''
    operater={'*':3,'/':3,'+':2,'-':2,'(':1}

    for i in exp:
        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZqwertyuiopasdfghjklzxcvbnm" or i in "0123456789":
            str+=i
        elif i == '(':
            s.push(i)
        elif i== ')':
            topS = s.pop()
            while topS != '(':
                str+=topS
                topS = s.pop()
        else:
            while not s.isEmpty() and  operater[s.peek()] >= operater[i]:
                str+= s.pop()
            s.push(i)
    while not s.isEmpty():
        str+=s.pop()
    return ''.join(str)


        



print(" ***Infix to Postfix***")

token = input("Enter Infix expression : ")

print("PostFix : ")

print(infix2postfix(token))