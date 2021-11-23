from collections import deque
'''
Big O 
เวลาเรียก queue จะมี2operation 1deque 2enqueue เวลาเอาไปใช้
อยู่ที่การimplementation
โปรแกรมที่ดี 1.ทำงานถูกต้อง 2.ทันใจ 3.ทรัพยากรที่ใช้รันได้ทุกเครื่อง(specคอมกาก)
4.ทำงานได้ตามต้องการ5.ความเสถียรของระบบ 6.Bugs

แพง คือ memory expansive ใช้หน่วยความจำเยอะ
	runtime expensive ใช้เวลาเยอะ
เลยเกิด queue linklist
โดยแต่ละอย่าง
- linklist มีcost มาเกี่ยว 
- dequeue ใช้ O(1) มันขึ้นกับว่าจำหน่วยตัวข้างในมี10ตัวใช้ 1ms 1ล้านตัวก็ใช้ 1ms
เรียกความเร็วคงที่ อีกชื่อ O(1) โอวัน โอหนึ่ง แต่มันในอุดมคติ
เวลาใใช้ linklist เก็บตัวชี้และ ข้อมูล มันเลยใช้ หน่วยความจำเป็น2เท่าของ list

Big O คือการวิเคราะห์ runing time complexityเปรียบเทียบสองตัวว่าตัวไหนมีประสิทธิภาพดีกว่า
แต่Big O ที่ดีกว่าไม่ได้เร็วกว่า เพราะ ขึ้นอยุกับ ความเร็วspecเครื่อง
n   T(n)
1    1ms
10   10ms
1M   1000s
T(N)ผันตามn เรียก O(n)
อีกเคส
n   T(n)
1    1
10   100
1M   1Ms
T(N) ผันตาม n^2,n^3,n! จะใช้เวลาเยอะมาก

เช่น ให้ทาย อันไหนเร็วสุด
1. O(1)	อันดับ1
2. O(n)	อันดับ3
3. O(n^2)	อันดับ4
4. O(logn)	อันดับ2



เวลาใช้ linklist จะมี3ขั้นตอนในการเชื่อม 1.สร้างnodeใหม่ 2.ลิ้งข้อมูลอันเก่ากะอันใหม่ 3.ลิ้งส่วนfront

radix sort ดูค่าในแต่ละหลัก
1.รับ input เก็บไว้ในqueue
2.หยิบตัวแรกออกไป
3.มันจะหาว่าตัวไหนmax และมีกี่หลัก
4.จะมีการเทียบ3รอบ รอบที่1 เอาข้อมูลที่ดึงออกมา เก็บไว้ตามหลักในรอบนั้นๆเช่น 64 เลขหลักหน่วยตรงกับหลัก4 ก้เก่บไว้ที่4
'''
class Queue:
    def __init__(self):
        self.items=deque()
    def enQueue(self,i):
        self.items.append(i)
    def deQueue(self):
        return self.items.popleft()
    def isEmpty(self):
        return len(self.items)==0
    def size(self):
        return len(self.items)
'''class Queue(): 
    def __init__(self,list=None):
        if list==None:
            self.items=[]
        else:
            self.items=list
    
    def enQueue(self,i):
        self.items.append(i)
    def deQueue(self):
        self.items.pop(0)
    def isQEmpty(self):
        return len(self.items)==0
    def size(self):
        return len(self.items)
'''
if __name__== '__main__':
    q=Queue()
    print(q.items)
    q.enQueue('A')
    print(q.items)
    q.deQueue()
    print(q.items)
    print(q.isEmpty())
