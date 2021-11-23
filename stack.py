'''stack เก็บข้อมูลซ้อนๆกัน Last in First out
 เอาของออกเรียกpop เอาอันบนสุดออก (ล่างคือตัวแรก)
Queue เข้าก่อนออกก่อน แถวคอย enqueue-เอาข้อมูลเข้า
                        dequeue-เอาข้อมูลออก''' 
class Stack():
    def __init__(self,list= None):
        if list==None:
            self.items=[]
        else:
            self.items=list
        
    def __str__(self):
        s='stack of '+str(self.size())+' items: '
        for ele in self.items:
            s+= str(ele)+' '
        return s

    def push(self,c):
        self.items.append(c)
        
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def isEmpty(self):
        #or len(self.items)==0
        return self.items == []
    def size(self):
        return len(self.items)

if __name__== '__main__':
    s=Stack([5,4])
    print(s.pop())
    s.push(8)
    print(s.items)
    print(s.size())
    print(s.peek())
    print(s.isEmpty())
    print(s)