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
#ES 1,ES 2,ES 3,D,D,D 
raw = input('Enter Input : ').split(',')
de=Queue()
tempS=[]
for i,x in enumerate(raw):
    num=[]
    #print(de,end=' ')
    toggle=False
    if raw[i][0] == 'E':
        for j in x:
            if j in "0123456789":
                num.append(j)
        #หน่วยพิเศษ
        temp=''.join(num)
        
        if raw[i][1]=='S': 
            if not de.isEmpty():
                if de.items[0][0]=='S':
                    #de.items.reverse()
                    while de.items[0][0]=='S':
                        tempS.append(de.deQueue())
                        #กันwhile error เพราะ หาindex ไม่เจอ
                        if de.size()==0:
                            de.enQueue('toggle')
                    if de.items[0]=='toggle':
                        de.deQueue()
                    de.items.reverse()
                    de.enQueue('S'+temp)
                    while tempS:
                        de.enQueue(tempS.pop())
                    de.items.reverse()
                    
                else:
                    de.items.reverse()
                    de.enQueue('S'+temp)
                    de.items.reverse()
                   
            else:
                de.items.reverse()
                de.enQueue('S'+temp)
                de.items.reverse()    
        #ไม่special       
        else:
            de.enQueue(temp)
    #print Display       
    else:
        if not de.isEmpty():
           
            #de.items.reverse()
            haveS=de.deQueue()
            #de.items.reverse()
            if haveS[0]=='S':
                for k in haveS:
                    if k in "0123456789":
                        num.append(k)
                temp=''.join(num)
                print(temp)
            else:
                print(haveS)
        else:
            print('Empty')