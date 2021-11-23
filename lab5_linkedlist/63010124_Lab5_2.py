'''
 * กลุ่มที่  : 21010001
 * 63010124 จักรภัทรณ์ ชื่นถาวร
 * chapter : 5	item : 2	ครั้งที่ : 0010
 * Assigned : Wednesday 8th of September 2021 09:02:45 AM --> Submission : Sunday 12th of September 2021 04:44:18 PM	
 * Elapsed time : 6221 minutes.
 * filename : 2.py
  ขอรบกวนอีกรอบด้วยครับ
'''
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s
        '''cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s'''

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        data = Node(item)
        if self.isEmpty():
            self.head = data
            self.tail = self.head
        else:
            pre = self.tail
            data.previous = pre
            pre.next = data
            self.tail = data
            '''cur = self.head
            while cur.next != None:
                cur=cur.next
            cur.next=Node(item)
            '''
    def addHead(self, item):
        data = Node(item)
        if self.isEmpty():
            self.head = data
            self.tail = self.head
        else:
            next = self.head
            next.previous = data
            data.next = next
            self.head = data

    def insert(self, pos, item):
        cur = self.head
        data= Node(item)
        if int(pos) == 0 :
            self.addHead(item)
        elif int(pos) > self.size():
            self.append(item)
        elif pos<0:
            #ถ้า -มากกว่าsize
            if abs(int(pos)) >= int(self.size()):
                
                self.addHead(item)
            # - ยังอยู่ในsize
            else:
                last=self.tail
                i=0
                while last.previous != None:
                    i-=1
                    if i==pos:#ชี้สองแขน
                        tempA = last.previous
                        data.previous = tempA
                        tempA.next=data
                        data.next = last
                        last.previous = data
                    last=last.previous
        #กรณีpos เป็นบวกปกติใน size
        else:
            i=0
            while cur.next != None:
                i+=1
                #Before : A-> B After : A-> C-> B(tempB)
                if i == pos:
                    tempB=cur.next
                    data.previous = cur
                    cur.next = data
                    tempB.previous= data
                    data.next = tempB
                cur=cur.next
    def search(self, item):
        cur =self.head
        while cur:
            if cur.value ==item:
                return 'Found'
            cur=cur.next
        return 'Not Found'

    def index(self, item):
        cur =self.head
        #ถ้าไม่มีข้อมูลในlist
        if cur is None:
            return 
        #if cur has one node
        if cur.value == item:
            return 0
        #if cur has more than one node
        i=0
        while cur:
            if cur.value == item:
                return i
            cur=cur.next
            i+=1
        return -1

    def size(self):
        if self.head is None:
            return 0
        cur=self.head
        count=1
        while cur.next != None:
            count+=1
            cur=cur.next
        return count
    def nodeAt(self,i) :              
        p = self.head
        for j in range(0,i) :
            p = p.next
        return p
    def pop(self, pos):
        cur=self.head
        count=0
        if abs(int(pos))>self.size():
            return 'Out of Range'
        
        if int(pos) == 0:
            if self.head is None:
                return 'Out of Range'
            if self.head.next is None:
                self.head = None
                return 'Success'
            self.head = self.head.next
            self.head.prev_node = None
        #ลบ tail ขอโทษครับพี่ ขอแก้ไขตรง i เป็น pos ครับ
        elif int(pos) == len(self)-2:
            q = self.nodeAt(pos)
            self.tail = q
        else:
            
            while cur.next != None:
                if count == pos:
                    cur.next= cur.next.next
                    return 'Success'
                count+=1
                cur=cur.next
            return 'Out of Range'
       
            
L = LinkedList()
print(L.index(2))
print(L)
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())