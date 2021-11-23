class Linkedlist:
    class Node:
        def __init__(self,data,next=None):
            self.data = data
            if next is None:
                self.next = None
            else:
                self.next = next
    def __init__(self):
        self.head=self.tail = None
        self.size=0
    def __str__(self):
        p=self.head
        s=''
        while p!=None:
            s+=str(p.data)+' '
            p=p.next
        return s
    def append(self,data):
        if self.head==None:
            self.head = self.Node(data)
        else:
            p=self.head
            while p.next!=None:
                p=p.next
            p.next=self.Node(data)
    def reverseIter(self,L):
        prev = None
        curr = self.head
        next = None
        while curr!= None:
            next = curr.next
            curr.next = prev
            prev=curr
            curr=next
        #prev is head node
        #print prev
        s=''
        while prev!=None:
            s+=str(prev.data)+' '
            prev=prev.next 
        return s
    def reverseRecur(self,head):
        if (self.head==None or self.head.next==None):
            return head
        reversed_list = reverseRecur(self.head.next)
        self.head.next.next = self.head
        head.next=None
        s=''
        while reversed_list!=None:
            s+=str(reversed_list.data)+' '
            reversed_list=reversed_list.next
        return s
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
def reverse(head):
    if (head ==None or head.next==None):
        return head
    list_to_do = head.next

    reversed_list=head
    reversed_list.next=None

    while list_to_do != None:
        temp=list_to_do
        list_to_do=list_to_do.next
        temp.next =reversed_list
        reversed_list = temp
    return reversed_list
        

l=Linkedlist()
for i in range(10):
    l.append(i)
print(l)
a=l.reverseIter(l)
print('a:',a)
lb=l.head
b=l.reverseRecur(lb)
s=''
while b!=None:
    s+=str(b.data)+' '
    b=b.next
print('b:',s)
lc=l.head
c=reverse(lc)
s=''
while c!=None:
    s+=str(c.data)+' '
    c=c.next
    #print(c.data)
print('c:',s)
l1=Linkedlist()
for i in range(5):
    l1.append(i)
print(l1)
l1.reversegg()
print(l1)