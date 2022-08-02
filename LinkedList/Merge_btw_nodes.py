# https://leetcode.com/problems/merge-in-between-linked-lists/
# Merge In Between Linked Lists

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        l1 = list1
        Head = l1
        B = b
        while Head:
            if B == 0:
                Head = Head.next
                break
            B -= 1
            Head = Head.next
            
        while l1.next:
            if a-1 == 0:
                # start of merge           
                l1.next = list2
            
            l1 = l1.next
            a -= 1
            
        l1.next = Head
        
        return list1