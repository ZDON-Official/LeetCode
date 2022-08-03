# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        List = []
        
        curr = head
        while curr:
            List.append(curr)
            curr = curr.next
        
        # for i in List:
        #     print(i.val)
            
        
        tmp = List[k-1].val
        # print("tmp-",tmp)
        # print("end-", List[-k].val)
        List[k-1].val = List[-k].val
        List[-k].val = tmp
        
        
        return head