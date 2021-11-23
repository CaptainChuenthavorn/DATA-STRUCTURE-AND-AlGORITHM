'''
 * กลุ่มที่  : 21010001
 * 63010124 จักรภัทรณ์ ชื่นถาวร
 * chapter : 3	item : 2	ครั้งที่ : 0002
 * Assigned : Wednesday 1st of September 2021 10:15:58 AM --> Submission : Wednesday 1st of September 2021 11:00:29 AM	
 * Elapsed time : 44 minutes.
 * filename : 63010124_Lab3_2.py
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

def parenMatch(raw):
    s = Stack()
    error=0
    open_paren=['(','[','{']
    close_paren=[')',']','}']
    for i in raw:
        if i in open_paren:
            s.push(i)
        else:
            if i in close_paren:
                if s.size()>0:
                    if not matchparen(s.pop(),i):
                        error = 1#open != close
                        return error,s
                else:
                    error = 2#close paren excess
                    return error,s
    if s.size()>0:
        error=3 # open paren excess
    return error,s

def matchparen(open,close):
    opens=['(','[','{']
    closes=[')',']','}']
    return opens.index(open)==closes.index(close)

if __name__== '__main__':
    print('Enter expresion :',end=' ')
    raw = input()
    err,s = parenMatch(raw)
    if err==1:
        print(raw,'Unmatch open-close')
    elif err==2:
        print(raw,'close paren excess')
    elif err==3:
        print(raw,'open paren excess  ',s.size(),':',''.join(s.items))
    else:
        print(raw,'MATCH')
