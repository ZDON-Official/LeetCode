# Swapping Nodes in a Linked List
# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        List = []
        # store the Nodes in a list
        curr = head
        while curr:
            List.append(curr)
            curr = curr.next           
        
        # swap the values of the nodes
        tmp = List[k-1].val
        List[k-1].val = List[-k].val
        List[-k].val = tmp
        
        return head

Sol = Solution()

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

k = 2

ans = Sol.swapNodes(head, 2)

while ans:
    print(ans.val)
    ans = ans.next