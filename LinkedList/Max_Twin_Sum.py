# Maximum Twin Sum of a Linked List
# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        maxSum = 0
        n = 0
        tmp = head
        while tmp:
            n += 1
            tmp = tmp.next
        
        TwinSum = {}
        
        curr = head
        index = 0
        currSum = 0
        while curr:
            if index in TwinSum:
                currSum = curr.val + TwinSum[index]
            else:
                TwinSum[n-1-index] = curr.val
            
            maxSum = max(maxSum, currSum)
            index += 1
            curr = curr.next
    
        return maxSum