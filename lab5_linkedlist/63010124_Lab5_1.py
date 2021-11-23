'''
 * กลุ่มที่  : 21010001
 * 63010124 จักรภัทรณ์ ชื่นถาวร
 * chapter : 5	item : 1	ครั้งที่ : 0005
 * Assigned : Wednesday 8th of September 2021 08:57:45 AM --> Submission : Saturday 11th of September 2021 10:44:53 AM	
 * Elapsed time : 4427 minutes.
 * filename : 1.py
 ขอรบกวนอีกรอบด้วยครับ
'''
class Node:
    def __init__(self,data=None,next=None):
        #node 1อันเก็บได้ 1 ชุด
        self.next = None
        self.data = data
class Singly_linked_list:
    def __init__(self,data):
        self.head = Node(data)#สร้าง head มา
    
    def insert(self,data):
        if self.head is None:
            data = Node(data)
            self.head = data
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(data)
    def delete(self,data):
        if self.search(data) is not True:
            return "Not in list"
        else:
            current = self.head #ตัวหัวสุด
            #ถ้าdataตรงกับhead
            if data == current.data:
                self.headd = self.head.next
            else:            
                while current is not None: #เดินหาไปจนกว่าจะnone
                    if current.next.data==data: # ถ้าเจอก้delete .next.next คือชี้ข้ามnode
                        current.next = current.next.next
                        break
                    else:
                        current = current.next
    def reverse(self):
        current = self.head
        previous,next=None,None
        while current:
            next=current.next #ตัวหลัง ชี้มาข้างหน้า
            current.next=previous#ตัวหน้า ชี้ไปหาnull(ตัวหลัง)
            previous=current#สลับ
            current=next

        self.head=previous
    def search(self,data):
        current=self.head
        
        while current is not None:
            if current.data ==data:
                return True
            else:
                current=current.next
                
        return False
    def length(self):
        cur=self.head
        total = 0
        while cur.next!=None:
            total+=1
            cur=cur.next
        return total
    def display(self):
        current = self.head 
        while current is not None:
            if current.data is not None:
                print(current.data, end=' ')
            current=current.next
        print()
    def isEmpty(self):
        cur=self.head
        total = 0
        while cur.next!=None:
            total+=1
            cur=cur.next
        return total==0
    def deleteNode(self,position):
        temp=self.head
        #if head will be removed
        if position==0:
            temp = self.head
            self.head = None
            return self.head
            self.head = temp.next
            temp=None
            return
        for i in range(position-1):
            temp = temp.next
            if temp is None:
                break
        #if position is more than number of node
        if temp is None:
            return
        if temp.next is None:
            return

        next =temp.next.next
        temp.next = None
        temp.next = next
def matchParen(ssl):
    openP=['(','[','{']
    closeP=[')',']','}']
    current = ssl.head
    i=0
    while current.next != None:
        if current.data in openP and current.next.data in closeP:
            x=openP.index(current.data)   
            if closeP.index(current.next.data) == x:
                ssl.deleteNode(i+1)
                ssl.deleteNode(i)
                i=0
            else:
                current=current.next
                i+=1
        else:
            current=current.next
            i+=1
ssl=Singly_linked_list(None)
raw=input('Enter Input : ')

for i in raw:
    ssl.insert(i)
    matchParen(ssl)
if not ssl.isEmpty():
    print('Parentheses : Unmatched ! ! !')
else:
    print('Parentheses : Matched ! ! !')
