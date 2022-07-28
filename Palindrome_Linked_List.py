# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        Head = head
        rev = []

        if Head == None:
            return False
        elif Head.next == None:
            return True
        else:
            while Head != None:
                rev.append(Head.val)
                Head = Head.next
            front = rev.copy()
            rev.reverse()

            print(front)
            print(rev)

            for i in range(len(front)):
                if front[i] != rev[i]:
                    return False
            
            #return True


        return True


sol = Solution()

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(1)

print(sol.isPalindrome(head)) # true