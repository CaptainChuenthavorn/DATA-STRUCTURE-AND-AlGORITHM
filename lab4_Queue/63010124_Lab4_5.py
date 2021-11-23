'''
 * กลุ่มที่  : 21010001
 * 63010124 จักรภัทรณ์ ชื่นถาวร
 * chapter : 4	item : 5	ครั้งที่ : 0002
 * Assigned : Saturday 4th of September 2021 09:06:33 AM --> Submission : Sunday 5th of September 2021 09:47:46 AM	
 * Elapsed time : 1481 minutes.
 * filename : 5.py
'''
class Queue:
    def __init__(self,list=None):
        if list==None:
            self.items=[]
        else:
            self.items=list
    def enQueue(self,i):
        self.items.append(i)
    def enQueueleft(self,i):
        self.items.insert(0,i)
    def deQueue(self):
        return self.items.pop(0)
    def deQueueleft(self):
        return self.items.pop(-1)
    def deQueueSpecial(self,i):
        self.items.pop(self.items.index(i))
    def deQueueSpecial2(self,i):
        for x in range(3):
            self.items.pop(self.items.index(i))
    def isEmpty(self):
        return len(self.items)==0
    def size(self):
        return len(self.items)
    
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
def colorCrush2(Normal,Mirror):
    qNormal=Queue()
    qMirror=Queue()
    normal_explosive=Queue()
    qReal=Stack()
    for i in Normal:
        qNormal.enQueue(i)
        
    reset=True
    while reset:
        reset=False
        #print('break')
        for i in range(len(qNormal.items)-2):
            #print(qNormal.items)
            if qNormal.items[i]==qNormal.items[i+1]==qNormal.items[i+2]:
                normal_explosive.enQueue(qNormal.items[i])
                qNormal.deQueueSpecial2(qNormal.items[i])
                reset=True
                break        
    count_before=normal_explosive.size()
    count_after=[]
    #flip mirror
    flip=Mirror[::-1]
    #find mirror explosion
    mirror_explosive=Queue()
    for i in flip:
        qMirror.enQueue(i)
    reset=True
    while reset:
        reset=False
        for i in range(len(qMirror.items)-2):
            if qMirror.items[i]==qMirror.items[i+1]==qMirror.items[i+2]:
                mirror_explosive.enQueue(qMirror.items[i])
                qMirror.deQueueSpecial2(qMirror.items[i])
                reset=True
                break
  
    count_mirror=[]
    for i in mirror_explosive.items:
        count_mirror.append(i)
    #look at Normal world
    #start over
    interupt2=0
    bomb=0
    for i in Normal:
        qReal.push(i)
        if mirror_explosive.isEmpty() and qReal.size()>=3:
            index=qReal.size()-1
            if  qReal.items[index]==qReal.items[index-1]==qReal.items[index-2] :
                for i in range(3):
                    qReal.pop()
                bomb+=1
        elif qReal.size()>=3:
            index=qReal.size()-1
            if  qReal.items[index]==qReal.items[index-1]==qReal.items[index-2] :
               
                temp2 = qReal.pop()
                qReal.push(mirror_explosive.deQueue())
                qReal.push(temp2)
                index=qReal.size()-1
                
                if  qReal.items[index]==qReal.items[index-1]==qReal.items[index-2]:
                    for i in range(3):
                        qReal.pop()
                    interupt2+=1
                    
    print('NORMAL :')
    print(qReal.size())
    if qReal.isEmpty():
        print('Empty')
    else:
        print(''.join(qReal.items[::-1]))
    print(bomb,'Explosive(s) ! ! ! (NORMAL)')
    if interupt2>0: 
        print(f'Failed Interrupted {interupt2} Bomb(s)')
    print('------------MIRROR------------\n: RORRIM')
    print(qMirror.size())
    if qMirror.isEmpty():
        print('ytpmE')
    else:
        print(''.join(qMirror.items[::-1]))
    print('(RORRIM) ! ! ! (s)evisolpxE',len(count_mirror))
    pass
if __name__== '__main__':
    Normal,Mirror= input('Enter Input (Normal, Mirror) : ').split()
    colorCrush2(Normal,Mirror)
    
    