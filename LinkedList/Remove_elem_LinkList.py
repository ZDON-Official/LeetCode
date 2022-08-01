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
        Curr = head
        Prev = None

        if head == None:
            return head
        
        while Curr:
            temp = Curr.next
            if Curr.val == val:
                if Prev != None:
                    Prev.next = Curr.next 
                else:
                    # head of the ListNode
                    Curr.next = None
                    head = temp
            else:
                Prev = Curr
            Curr = temp
        
        return head



    def removeElements2(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        while head:
            if head.val == val:
                head = head.next
                continue
            
            curr.next = head
            curr = curr.next
            head = head.next
        
        curr.next = None
        return dummy.next

sol = Solution()

head = ListNode(2)
head.next = ListNode(1)
head.next.next = ListNode(3)
head.next.next.next = ListNode(7)

ans = sol.removeElements(head, 7)

while ans:
    print(ans.val)
    ans = ans.next