class Solution {
public:
    vector<int> printListFromTailToHead(ListNode* head) {
        vector<int> array;
        if(head!=NULL)
        {
            array.insert(array.begin(),head->val);
            while(head->next!=NULL)
            {
                array.insert(array.begin(),head->next->val);
                head=head->next;
            }
        }
        return array;
    }
};