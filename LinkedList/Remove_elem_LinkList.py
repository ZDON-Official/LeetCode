# https://leetcode.com/problems/remove-linked-list-elements/
# Remove Linked List Elements

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        Head = head
        Prev = None

        if head == None:
            return head
        
        while Head:
            temp = Head.next
            if Head.val == val:
                if Prev != None:
                    Prev.next = Head.next 
                else:
                    # head of the ListNode
                    Head.next = None
                    head = temp
            else:
                Prev = Head
            Head = temp
        
        return head

sol = Solution()

head = ListNode(7)
head.next = ListNode(7)
head.next.next = ListNode(7)
head.next.next.next = ListNode(7)

ans = sol.removeElements(head, 7)

print("------------------------------------------------")
while ans:
    print(ans.val)
    ans = ans.next