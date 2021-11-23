class Queue():
    def __init__(self,list=None):
        if list==None:
            self.list=[]
        else:
            self.list = list
    def enqueue(self,data):
        self.list.append(data)
    def dequeue(self):
        return self.list.pop(0)
    def isEmpty(self):
        return len(self.list) ==0
    def __str__(self):
        return ''.join(str(self.list))
def radixSort(lst):
    q=Queue(lst)
    max_digit=getMaxDigit(lst)
    q10=[Queue(),Queue(),Queue(),Queue(),Queue(),Queue(),Queue(),Queue(),Queue(),Queue()]
    for i in range(1,max_digit+1):
        while not q.isEmpty():
            num=q.dequeue()
            indexDigit=getDigit(num,i)
            q10[indexDigit].enqueue(num)
        print('\nQQ:',end=' ')
        for i in range(10):
            print(q10[i],end=' ')
        for j in range(10):
            
            while not q10[j].isEmpty():
                q.enqueue(q10[j].dequeue())
    return q.list
def getDigit(n,d):
    for i in range(d-1):
        n//=10
    return n%10
def getMaxDigit(lst):
    n=max(lst)
    i=0
    while n>0:
        n//=10
        i+=1
    return i

lst=[64,8,216,512,27,729,0,1,343,125]
a=radixSort(lst)
print(a)