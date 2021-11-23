'''
 * กลุ่มที่  : 21010001
 * 63010124 จักรภัทรณ์ ชื่นถาวร
 * chapter : 4	item : 3	ครั้งที่ : 0005
 * Assigned : Friday 3rd of September 2021 05:19:16 PM --> Submission : Saturday 4th of September 2021 12:53:30 PM	
 * Elapsed time : 1174 minutes.
 * filename : 3.py
'''
#i love Python,256183

'''
q1 = Queue(string)

q2 = Queue(number)

encodemsg(q1, q2)

decodemsg(q1, q2)
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

def encode(qA,qNum):
    ans=[]
    decode=[]
    toggle=False
    while len(qA.items) != 0:
        alphabet=qA.deQueue()
        decode.append(alphabet)
        num=qNum.deQueue()
        if alphabet.isupper():
            alphabet=alphabet.lower()
            toggle=True
        if ord(alphabet)+num>122:
            temp=122-ord(alphabet)
            la=num-temp
            last=96+la
            if toggle:
                ans.append(chr(last).upper())
            else:
                ans.append(chr(last))
        else:
            last=ord(alphabet)+num
            if toggle:
                ans.append(chr(last).upper())
            else:
                ans.append(chr(last))
        qNum.enQueue(num)
        toggle=False
    return ans,decode
raw=input('Enter String and Code : ').split(',')
qA=Queue()
qNum=Queue()
for word in raw:
    for i in word:
        if i in "0123456789":
            qNum.enQueue(int(i))
        elif i==' ':
            pass
        else:
            qA.enQueue(i)
qA.items
ans,decode=encode(qA,qNum)
print('Encode message is : ',ans)
print('Decode message is : ',decode)