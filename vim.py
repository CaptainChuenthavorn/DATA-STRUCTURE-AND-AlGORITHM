from typing import Sized


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
            
raw =input('Enter Input : ').split(',')
L1 = SinglyLinkedListNoDummy()
L1.append('|')
for i in raw:
    if i[0]=='I':
        numCur=L1.indexOf('|')
        L1.delete(numCur)
        if numCur==0:
            L1.addHead(i[2:])
        else:
            L1.insertAfter(numCur-1,i[2:])
        L1.insertAfter(numCur,'|')
        
    elif i[0]=='L':
        numCur = L1.indexOf('|')
        L1.delete(numCur)
        if numCur==0 or numCur==1:
            L1.addHead('|')
            pass
        else:
            L1.insertAfter(numCur-2,'|')
        
    elif i[0]=='R':
        numCur = L1.indexOf('|')
        if numCur==L1.size-1:
            pass
        else:
            L1.delete(numCur)
            L1.insertAfter(numCur,'|')
    elif i[0]=='B':
        numCur = L1.indexOf('|')
        if numCur==0:
            pass
        else:
            L1.delete(numCur-1)

    else:
        numCur = L1.indexOf('|')
        if numCur==L1.size-1:
            pass
        else:
            L1.delete(numCur+1)
print(L1)
