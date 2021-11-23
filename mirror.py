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
    
 
def colorCrush2(Normal,Mirror):
    qNormal=Queue()
    qMirror=Queue()
    normal_explosive=Queue()
    qReal=Queue()
    for i in Normal:
        qNormal.enQueue(i)
        qReal.enQueue(i)
    print(qNormal.items)
    '''for i in range(qNormal.size()):
        index=qNormal.size()-1
        
        if qNormal.size()>=3 and qNormal.items[index]==qNormal.items[index-1]==qNormal.items[index-2]:
            normal_explosive.enQueue(qNormal.items[index])
            qNormal.deQueueleft()
            qNormal.deQueueleft()
            qNormal.deQueueleft()'''
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
    
    print('normalexplo',normal_explosive.items)
    
    
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
    '''for index,i in enumerate(qMirror.items):
        index=qMirror.size()-1
        if qMirror.size()>=3 and qMirror.items[index]==qMirror.items[index-1]==qMirror.items[index-2]:
            qMirror.deQueueleft()
            qMirror.deQueueleft()
            qMirror.deQueueleft()
            mirror_explosive.enQueue(i)'''
    print('miir',mirror_explosive.items)
    count_mirror=[]
    for i in mirror_explosive.items:
        count_mirror.append(i)
    
    #look at Normal world
    #start over
    interupt2=0
    reset=True
    G=0
    while reset:
        G+=1
        Gcount=0
        reset=False
        if G>10:
            reset=True
            break
        for i in range(qReal.size()-3):
            
            print(i,'size',qReal.size(),'qReal:',qReal.items)
            if qReal.items[i]==qReal.items[i+1]==qReal.items[i+2]:
                Gcount+=1
                #mirror not empty add interupt
                if not mirror_explosive.isEmpty():
                    if qReal.items[i]==normal_explosive.items[0]:
                        #if first letter didn't have 3
                        temp=[]
                        while qReal.items[0]!=normal_explosive.items[0]:
                            temp.append(qReal.deQueue())
                            print('remove:',qReal.items)
                        qReal.deQueue()
                        qReal.deQueue()
                        qReal.enQueueleft(mirror_explosive.deQueue())
                        qReal.enQueueleft(normal_explosive.items[0])
                        qReal.enQueueleft(normal_explosive.items[0])
                        if qReal.items[i]==qReal.items[i+1]==qReal.items[i+2]:
                            qReal.deQueueSpecial2(qReal.items[i])
                            print('interupt2')
                            interupt2+=1
                        for omg in range(len(temp)):
                            if temp==[]:
                                pass
                            else:
                                qReal.enQueueleft(temp.pop(0))
                                print('add',qReal.items)
                        
                #mirror don't have anything to interupt
                else:
                    if qReal.items[i]==qReal.items[i+1]==qReal.items[i+2]:
                        count_after.append(qReal.items[i])
                        qReal.deQueueSpecial2(qReal.items[i])
                        normal_explosive.deQueue()
                if Gcount==3:
                    reset=True
                    break
            
        
    #check count
    interupt=0

    for al in count_after:
        if al in count_mirror:
            interupt+=1
    print('NORMAL :')
    print(qReal.size())
    if qReal.isEmpty():
        print('Empty')
    else:
        print(''.join(qReal.items[::-1]))
    
    print(len(count_after),'Explosive(s) ! ! ! (NORMAL)')
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
    
    