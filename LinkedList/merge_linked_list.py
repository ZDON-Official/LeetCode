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
        curr  = merged

        # while the two listNode are not None loop over them
        while list1 and list2:
            
            if list1.val > list2.val:
                curr.next = list2
                list2 = list2.next
            elif list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                # both val are equal
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        curr.next = list1 or list2

        return merged.next