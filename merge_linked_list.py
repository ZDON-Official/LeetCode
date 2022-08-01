# Merge Two Sorted List
#https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = ListNode(0)

        # while the two listNode are not None loop over them
        while list1 or list2:
            
            
            # set the two lists to .next if it is not None
            list1 = list1.next if list1 else None
            list2 = list2.next if list2 else None


        return merged