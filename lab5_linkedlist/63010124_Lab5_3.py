'''
 * กลุ่มที่  : 21010001
 * 63010124 จักรภัทรณ์ ชื่นถาวร
 * chapter : 5	item : 3	ครั้งที่ : 0001
 * Assigned : Wednesday 8th of September 2021 09:02:51 AM --> Submission : Monday 13th of September 2021 12:15:04 PM	
 * Elapsed time : 7392 minutes.
 * filename : 3.py
'''
class node:
    def __init__(self,data,next = None ):
        self.data = data
        self.next = next
    def __str__(self):
        
        return self.data

def createList(l=[]):
    #create head node and current node to add new node
    head_node = node(None)
    current = head_node
    #sort l
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]
    for i in l:
        new_node = node(i)
        current.next = new_node
        current = current.next
    #reset current to head again
    current = head_node
    while current.next != None:
        current=current.next
    return head_node.next

def printList(H):
    s=''
    #h.next because skip None of head data
    current = H
    #current=current.next
    while current:
        s+=str(current.data)+' '
        current=current.next
    print(s)
    return 

def mergeOrderesList(p,q):
    result = node(None)
    if q==None:
        return p
    if p==None:
        return q
    
    if p.data <= q.data:
        result = p
        result.next = mergeOrderesList(p.next,q)
    else:
        result = q
        result.next = mergeOrderesList(p,q.next)
    return result

#################### FIX comand ####################   
# input only a number save in L1,L2
L1,L2 = input('Enter 2 Lists : ').split()
L1 = [int(x) for x in L1.split(',')]
L2 = [int(x) for x in L2.split(',')]
LL1 = createList(L1)
LL2 = createList(L2)
print('LL1 : ',end='')
printList(LL1)
print('LL2 : ',end='')
printList(LL2)
m = mergeOrderesList(LL1,LL2)
print('Merge Result : ',end='')
printList(m)