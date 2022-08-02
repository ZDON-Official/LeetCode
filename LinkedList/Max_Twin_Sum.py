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
        
        curr = head
        i = 0
        j = 0
        twinNode = 0

        twinSum = {}

        while curr.next:
            curr2 = curr.next
            twinNode = (n-1-i)
            j = i+1
            
            while curr2:
                if i <= (n/2)-1 and j == twinNode:
                    currSum = curr.val + curr2.val    
                j += 1
                curr2 = curr2.next
            maxSum = max(maxSum, currSum)
            i += 1
            curr = curr.next
        
        return maxSum