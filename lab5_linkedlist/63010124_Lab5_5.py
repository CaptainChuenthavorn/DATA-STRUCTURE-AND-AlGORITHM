'''
 * กลุ่มที่  : 21010001
 * 63010124 จักรภัทรณ์ ชื่นถาวร
 * chapter : 5	item : 5	ครั้งที่ : 0007
 * Assigned : Wednesday 8th of September 2021 09:02:54 AM --> Submission : Thursday 16th of September 2021 08:42:29 PM	
 * Elapsed time : 12219 minutes.
 * filename : 5.py
'''

class SinglyLinkedListNoDummy :     # ทำงานเหมือนกับ List (อ้าง อินเด็กซ์แบบเดียวกัน)
    class Node :                    # โหนดเก็บข้อมูล
        def __init__(self, data, next = None) :
            self.data = data
            if next is None :
                self.next = None
            else :
                self.next = next

    def __init__(self):                
            self.head = None
            self.size = 0
            
    def __str__(self):                # แสดงข้อมูลทุกตัวใน linked list
        s = ''
        p = self.head
        while p != None :
            s += str(p.data) + ' '
            p = p.next
        return s
          
    def __len__(self) :               # เพิ่ม เมื่อ เติมข้อมูล  ลด เมื่อ นำข้อมูลออก
        return self.size         
            
    def isEmpty(self) :               # ตรวจสอบว่ามีข้อมูลใน linked list ไหม
        return self.size == 0         # len(self) == 0
        
    def indexOf(self,data) :          # หา อินเด็กของข้อมูลว่าอยู่ที่ตำแหน่งใด
        p = self.head
        for i in range(len(self)) :
            if p.data == data :
                return i
            p = p.next
        return -1
            
    def isIn(self,data) :             # ตรวจสอบว่าใน linked list นี้ มีข้อมูลตัวนี้ไหม
        return self.indexOf(data) >= 0
    
    def nodeAt(self,i) :              # หาค่าตำแหน่งของโหนด เทียบกับ อินเด็กซ์
        p = self.head
        for j in range(0,i) :
            p = p.next
        return p
    
    def append(self,data):           # เพิ่ม ข้อมูล ไปที่ด้านท้ายของ linked list
        if self.head is None :
          p = self.Node(data)
          self.head = p
          #self.head = self.Node(data,None)
          self.size += 1
        else :                        # เพิ่ม ในกรณีที่ไม่ใช่ Node แรก
          self.insertAfter(len(self)-1,data)   #len(self) = จำนวนสมาชิก - 1 คือ index
          
    def insertAfter(self,i,data) :       #เพิ่ม ข้อมูล ในสายข้อมูลที่มีอยู่แล้ว
        q = self.nodeAt(i)
        p = self.Node(data)
        p.next = q.next
        q.next = p
        #q.next = self.Node(data,q.next)
        self.size += 1

    def removeTail(self) :
        if self.size > 0 :
          q = self.nodeAt(len(self)-2)
          self.tail = q
          q.next = None
          self.size -= 1

    def deleteAfter(self,i) :            #ลบ โหนดข้อมูล ในสายข้อมูลที่มีอยู่แล้ว
        if self.size > 0 :  # len(self)
          q = self.nodeAt(i)  
          if i == len(self)-2 :
            self.tail = q
          q.next = q.next.next
          self.size -= 1
    
    def delete(self,i) :                 #ลบข้อมูลที่ อินเด็กซ์ที่กำหนด
        if i == 0 and self.size > 0 :    #ลบตัวแรก
          self.head = self.head.next
          self.size -= 1
        else :
          self.deleteAfter(i-1)          #ลบตัวก่อนหน้า
        
    def removeData(self,data) :          #ลบข้อมูลใน linked list
        if self.isIn(data) :
            self.deleteAfter(self.indexOf(data)-1)
          
    def addHead(self,data) :
        if self.isEmpty() :
          p = self.Node(data)
          self.head = p
          #self.head = self.Node(data,None)
          self.size += 1
        else :
          p = self.Node(data,self.head)
          self.head = p
          self.size += 1
    def checkTree(self,poison):
        if self.head == None:
           return 0
        cur = self.head
        cur_next = self.head #index0
        cur_next=cur_next.next #index1
        count=1
        #if list have 1 term
        if cur_next.next is None:
            return 1
        #index even
        if poison:
            cur_next=cur_next.next #index2
        #index odd
        else:
            cur=cur.next#index1
            cur_next=cur_next.next#index2
            cur_next=cur_next.next#index3
        #print('curnext .data',cur_next.data)
        min = cur.data
        #print('count start',count)
        while cur_next.next is not None:
            #ถ้าข้างหลังน้อยกว่าให้เปลี่ยนmin และ count++
            if min < cur_next.data:
                
                count+=1
                min = cur_next.data
            #เลื่อนcur ไป2ตำแหน่ง
            cur= cur.next
            cur= cur.next
            #เลื่อน cur next 1ตำแหน่งและถ้าอีกตำแหน่งเป็น none ตัดจบ
            cur_next=cur_next.next
            if cur_next.next is None:
                return count
            cur_next=cur_next.next
        if min < cur_next.data:
            count+=1
        return count
        
'''
กราบขอโทษจริงๆครับพี่ ผมไม่รอบคอบเองครับ ครั้งหน้าจะปรับปรุงครับพี่
'''
if __name__== '__main__':
    raw=input('Enter Input : ').split(',')
    L1=SinglyLinkedListNoDummy()
    poison=False
    toggle = True
    for i in raw:
        if i[:1]=='A':
            #odd
            num = int(i[2:])
            if num%2==1:
                L1.addHead(num)
                L1.addHead(num+2)
            #even
            else:
                L1.addHead(num)
                L1.addHead(num-1)
        elif i[:1]=='B':
            
            ans = L1.checkTree(poison)
            
            poison=False
            print(ans)
        #sจะอยุ่ข้างหน้า indexเป้นeven แบบปกติจะอยุหลังเป็น 1
        elif i[:1]=='S':
            if poison:
                poison=False
            else:
                poison=True