
//Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
 
class Solution {
    public:
        ListNode* mergeNodes(ListNode* head) {
            int merge = 0;
            for(auto *ptr = head, *ptr2 = head->next; ptr2 != nullptr; ptr2 = ptr2->next){
                if(ptr2->val == 0){
                    ptr = ptr->next;
                    ptr->val = merge;
                    
                    merge = 0;
                } else{
                    merge += ptr2->val;
                }
            }
            return head->next;
        }
};

int main(int argc, char const *argv[])
{
    
    ListNode l = ListNode();
    l.next = new ListNode(3);
    l.next->next = new ListNode(1);
    l.next->next->next = new ListNode();
    l.next->next->next->next = new ListNode(4);
    l.next->next->next->next->next = new ListNode(5);
    l.next->next->next->next->next->next = new ListNode(2);
    l.next->next->next->next->next->next->next = new ListNode();


    return 0;
}
