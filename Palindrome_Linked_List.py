# Definition for singly-linked list.
from asyncio.windows_events import NULL
from email.header import Header
from operator import truediv
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        Head = head
        rev = []

        if Head == NULL:
            return False
        elif Head.next == None:
            return True
        else:
            while Head != None:
                rev.append(Head.val)
                Head = Head.next
            rev.reverse()
        
        return False


sol = Solution()

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)

# rev = []
# temp = head

# while temp != None:
#     rev.append(temp.val)
#     temp = temp.next
# rev.reverse()

# print(rev)

print(sol.isPalindrome(head)) # true