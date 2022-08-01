# Definition for singly-linked list.
from random import betavariate
from tkinter.messagebox import NO
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp2 = head.next
        temp = head
        merge = 0
        

        while temp2.next != None:

            merge += temp2.val
            temp2 = temp2.next

            if temp2.val == 0:
                temp = temp.next
                temp.val = merge
                merge = 0

        temp.next = None
        return head.next


sol = Solution()

h = ListNode()
h.next = ListNode(3)
h.next.next = ListNode(1)
h.next.next.next = ListNode()
h.next.next.next.next = ListNode(4)
h.next.next.next.next.next = ListNode(5)
h.next.next.next.next.next.next = ListNode(2)
h.next.next.next.next.next.next.next = ListNode()

# temp = h
# while temp.next != None:
#     print(temp.val)
#     temp = temp.next


ans = sol.mergeNodes(h)

while ans:
    print(ans.val)
    ans = ans.next