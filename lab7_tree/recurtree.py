# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = cur = listNode()
        carryout=0
        while l1 or l2:
            d=carryout
            if l1 and l2:
                d+= (l1.val+l2.val)
                l1=l1.next
            elif l1:
                d+=l1.val
                l1=l1.next
            elif l2:
                d+=l2.val
                l2=l2.next
            carryout=d//10
            cur.next=List(d%10)
            cur=cur.next
        return dummy.next

