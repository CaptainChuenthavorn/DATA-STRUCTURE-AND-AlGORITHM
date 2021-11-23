'''
 แก้ครั้งใหม่ครับ ขอรบกวนด้วยนะครับ
 * กลุ่มที่  : 21010001
 * 63010124 จักรภัทรณ์ ชื่นถาวร
 * chapter : 4	item : 2	ครั้งที่ : 0006
 * Assigned : Friday 3rd of September 2021 04:13:09 PM --> Submission : Friday 3rd of September 2021 10:18:22 PM	
 * Elapsed time : 365 minutes.
 * filename : 2.py
'''
class Queue:
    def __init__(self,list=None):
        if list==None:
            self.items=[]
        else:
            self.items=list
    def enQueue(self,i):
        self.items.append(i)
    def deQueue(self):
        return self.items.pop(0)
    def deQueueleft(self):
        return self.items.pop(-1)
    def isEmpty(self):
        return len(self.items)==0
    def size(self):
        return len(self.items)
    def peek(self):
        return self.items[len(self.items)-1]   
    def __str__(self):
        return ' '.join(str(self.items)) 
#ES 1,ES 2,ES 3,D,D,D 
raw = input('Enter Input : ').split(',')
#special
qS=Queue()
qN=Queue()

tempS=[]
for i,x in enumerate(raw):
    sumQ=Queue()
    if raw[i][0]=='E':
        if raw[i][1]=='S':
            qS.enQueue(raw[i][3:])
        elif raw[i][1]=='N':
            qN.enQueue(raw[i][3:])
        #print('S',qS,qS.size())
        #print('N',qN,qN.size())
    #display
    else:
        if not qN.isEmpty() or not qS.isEmpty():
            #list qS is not empty
            if qS.items:
                print(qS.deQueue())
            else:
                print(qN.deQueue())
        else:
            print('Empty')