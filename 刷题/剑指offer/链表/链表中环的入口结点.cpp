# 先找到在环中相遇的结点，然后设两个指针分别从起点和相遇结点出发，
# 再次相遇时，就在环的入口结点
class Solution
{
public:
    ListNode* MeetingNode(ListNode* pHead)
    {
        ListNode* fast = pHead;
        ListNode* slow = pHead;

        ListNode* fast;
        ListNode* slow;
        fast = slow = pHead;

        while(slow!=NULL && fast->p_mNext!=NULL)
        {
            slow = slow->p_mNext;
            fast = fast->p_mNext->p_mNext;
            if(slow == fast)
                return slow;
        }
        return NULL;
    }
    ListNode* EntryNode(ListNode* pHead)
    {
        ListNode* meetingNode = MeetingNode(pHead);
        if(pHead == NULL)
            return NULL;
        ListNode* p1=pHead;
        ListNode* p2=meetingNode;
        while(p1!=p2)
        {
            p1 = p1->p_mNext;
            p2 = p2->p_mNext;
        }
        return p1;
    }
}