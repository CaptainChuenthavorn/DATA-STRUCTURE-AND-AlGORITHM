'''
 * กลุ่มที่  : 21010001
 * 63010124 จักรภัทรณ์ ชื่นถาวร
 * chapter : 4	item : 1	ครั้งที่ : 0005
 * Assigned : Friday 3rd of September 2021 11:04:52 AM --> Submission : Friday 3rd of September 2021 10:25:37 PM	
 * Elapsed time : 680 minutes.
 * filename : 1.py
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
    def isEmpty(self):
        return len(self.items)==0
    def size(self):
        return len(self.items)
#E 1,E 2,E 3,D,D,E 4
if __name__== '__main__':
    q=Queue()
    deq=[]
    raw=input('Enter Input : ').split(',')
    for index,x in enumerate(raw):
        if raw[index][0]=='E':
            
            q.enQueue(raw[index][2])
            print(', '.join(q.items))
        else:
            if q.isEmpty():
                print('Empty')
                pass
            else:
                deq.append(q.deQueue())
                if q.isEmpty():
                    print(', '.join(deq[-1]),'<-','Empty')
                else:
                    print(', '.join(deq[-1]),'<-',', '.join(q.items))
    if q.isEmpty():
        if len(deq)==0:
            print('Empty',':','Empty')
        else:
            print(', '.join(deq),':','Empty')
    else:
        if len(deq)==0:
            print('Empty',':',', '.join(q.items))
        else:
            print(', '.join(deq),':',', '.join(q.items))