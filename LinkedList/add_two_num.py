# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        
        l1_s = ""
        l2_s = ""
        
        while l1:
            l1_s += str(l1.val)
            l1 = l1.next
        while l2:
            l2_s += str(l2.val)
            l2 = l2.next
        
        l1_s = int(l1_s[::-1])
        l2_s = int(l2_s[::-1])
            
        ans = str(l1_s + l2_s)[::-1]
        
        for c in ans:
            newNode = ListNode(int(c))
            curr.next = newNode
            curr = newNode
            
        return dummy.next