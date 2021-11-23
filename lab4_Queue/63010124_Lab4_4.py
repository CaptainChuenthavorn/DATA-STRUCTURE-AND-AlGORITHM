'''
 * กลุ่มที่  : 21010001
 * 63010124 จักรภัทรณ์ ชื่นถาวร
 * chapter : 4	item : 4	ครั้งที่ : 0005
 * Assigned : Saturday 4th of September 2021 09:06:32 AM --> Submission : Sunday 5th of September 2021 03:24:53 PM	
 * Elapsed time : 1818 minutes.
 * filename : 4.py
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

if __name__== '__main__':
    rawL,rawR = input('Enter Input : ').split('/')
    left=[str(x) for x in rawL.split(',')]
    right=[str(x) for x in rawR.split(',')]
    lef=[i.split() for i in left]
    dict={lef[i][1]:lef[i][0] for i in range(0,len(lef),1)}
    id=Queue()
    rank=Queue()
    tempID=Queue()
    tempRank=Queue()
    for i,x in enumerate(right):
        if right[i][0]=='E':
            
            num=right[i].split()[1]
            if dict[num] in rank.items:
                if id.items.count(num) == id.size():
                    rank.enQueue(dict[num])
                    id.enQueue(num)
                else:
                
                    while rank.peek()!=dict[num]:
                    #while id.items.count(num) != id.size():
                        tempID.enQueue(id.deQueueleft())
                        tempRank.enQueue(rank.deQueueleft())
                    rank.enQueue(dict[num])
                    id.enQueue(num)
                    while tempID.items:
                        rank.enQueue(tempRank.deQueueleft())
                        id.enQueue(tempID.deQueueleft())
            else:
                rank.enQueue(dict[num])
                id.enQueue(num)
        #D
        else:
            if rank.isEmpty():
                print('Empty')
            else:
                print(id.deQueue())
                rank.deQueue()

'''
โรงอาหารของบริษัทแห่งหนึ่ง จะมีเจ้าหน้าที่คอยจัดแถวสำหรับการซื้ออาหาร 
โดยจะมีหลักการคือจะดูจากแผนกของพนักงานแต่ละคนว่าอยู่แผนกไหน 
ถ้าหากในแถวที่ต่ออยู่มีแผนกนั้น จะนำพนักงานคนนั้นแทรกไปด้านหลังของแผนกเดียวกัน ตัวอย่างเช่น
Front | 1 2 2 2 2 3 3 3 | Rear  จาก Queue ถ้าหากมีพนักงานแผนก1เข้ามา Queue 
จะกลายเป็น Front | 1 1 2 2 2 2 3 3 3 | Rear

Input :
จะแบ่งเป็น 2 ฝั่งแบ่งด้วย /   คือ 
ซ้าย : เป็นแผนกของพนักงานและIDของพนักงานแต่ละคน  ขวา : จะแบ่งเป็น 2 ส่วน คือ D กับ E
E < id >  ->   เป็นการนำพนักงานเข้า Queue
D  ->  เป็นการนำพนักงานคนหน้าสุดออกจากแถว โดยจะแสดงผลเป็น id ของพนักงานคนนั้น 
ถ้าหากไม่มีพนักงานในแถวจะทำการแสดงผลเป็น Empty

อธิบาย TestCase_1 :  จะมีพนักงาน 4 คน คือแผนก 1 id=101,102 
และแผนก 2 id=201,202  ต่อมาจะแสดงผล Empty เพราะยังไม่มีพนักงานในแถว  
และนำพนักงาน id=101และ201 เข้าแถวตามลำดับ ต่อมาจะแสดงผลเป็น 101 
เพราะพนักงาน 101 อยู่คนแรกและแสดงผล 201 เพราะอยู่คนแรก
Enter Input : 1 101,1 102,2 201,2 202/D,E 101,E 201,D,D
Empty
101
201

'''