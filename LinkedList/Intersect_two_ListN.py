# https://leetcode.com/problems/intersection-of-two-linked-lists/
# Intersection of Two Linked Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        A = headA
        B = headB
        setA = set()
        
        while A:
            setA.add(A)
            A = A.next
        
        while B:
            if B in setA:
                return B
            B = B.next
        
        return None