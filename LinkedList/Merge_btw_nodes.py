# https://leetcode.com/problems/merge-in-between-linked-lists/
# Merge In Between Linked Lists

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        merged = ListNode(0)
        curr = merged.next
        
        l1 = list1
        l2 = list2
        Head = l1
        B = b
        while Head:
            if B == 0:
                Head = Head.next
                break
            B -= 1
            Head = Head.next # tail
            
        print("head val - ",Head.val)
        
        
        while l1.next:
            if a-1 == 0:
                # start of merge
                print("staring merge-", l1.val)
                #Head = l1.next
                l1.next = list2
                #print("next-", l1.next.val)
            if a == 0 and b > 0:
                # end of merge
                #print("end merge-", l1.val, b)
                #Head = Head.next
                pass
            
            l1 = l1.next
            a -= 1
            b -= 1
            
        l1.next = Head
        
        #print("val-", l1.val)
        
        
        
        return list1