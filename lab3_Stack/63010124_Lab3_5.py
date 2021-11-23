'''
 แก้อีกรอบครับผม5555 ขอบคุณล่วงหน้านะครับพี่
 * กลุ่มที่  : 21010001
 * 63010124 จักรภัทรณ์ ชื่นถาวร
 * chapter : 3	item : 5	ครั้งที่ : 0002
 * Assigned : Thursday 2nd of September 2021 02:16:19 PM --> Submission : Friday 3rd of September 2021 10:46:42 AM	
 * Elapsed time : 1230 minutes.
 * filename : 63010124_Lab3_5.py
'''
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
    def peek(self):
        return self.items[len(self.items)-1]

def parking(maxParkingSpace, numberOfCar, order, carNum):
    s=Stack()
    numberOfCar = [int(x) for x in numberOfCar.split(',')]
    temp=[]
    for i in numberOfCar[::-1]:
        s.push(i)
    
    for i in s.items:
        if 0 in s.items:
            s.pop()
        if order[0] == 'a':
            if carNum in s.items:
                return f'car {carNum} already in soi',s.items
            elif s.size() == maxParkingSpace:
                return f'car {carNum} cannot arrive : Soi Full',s.items 
            else : 
                s.items.reverse()
                s.push(carNum)
                s.items.reverse()
                return f'car {carNum} arrive! : Add Car {carNum}',s.items  
        else:
            if s.isEmpty():
                return f'car {carNum} cannot depart : Soi Empty',s.items
            if carNum not in s.items:
                return f'car {carNum} cannot depart : Dont Have Car {carNum}',s.items
            else:
                while carNum in s.items:
                    temp.append(s.pop())
                temp.pop()
                while temp:
                    s.push(temp.pop())

                    
                return f'car {carNum} depart ! : Car {carNum} was remove',s.items 
            
    return 0
        
    

print("******** Parking Lot ********")
m,s,o,n = input("Enter max of car,car in soi,operation : ").split()


m,n = int(m),int(n)
description,lst=parking(m,s,o,n)
print(description)
print(lst[::-1])
### Enter Your Code Here ###

'''
1.maxParkingSpace 2.numberOfCar 3.Order 4.carNum
car n arrive! : Add car n
car n cannot arrive : Soi Full
car n already in soi
car 7 arrive! : Add Car 7
car 3 cannot depart : Soi Empty
car 1 depart ! : Car 1 was remove
car 1 cannot depart : Dont Have Car 1
car 7 depart ! : Car 7 was remove
car 1 arrive! : Add Car 1

car n arrive! (ตรวจว่าซอยเต็มยัง ยังไม่เตมadd car)	Add car n (A:ไม่มีcarในs)
car n cannot arrive	(ซอยเต็ม)			Soi Full (A:lenเกินmax)
car n already in soi	(ดูในsก่อน)			Soi Empty (D:)
car n depart !	(ถ้ามีก้ลบออก)		Car 1 was remove (D:)
car n cannot depart (เชคก่อนว่าsมีไหม)		Dont Have Car 1 (D:)
'''