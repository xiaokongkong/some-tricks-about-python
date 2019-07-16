class Solution{
public:
    ListNode* deleteDuplication(ListNode* pHead)
    {
        if(pHead == NULL)
            return NULL;
        ListNode* pPre = NULL;
        ListNode* pCur = pHead;
        ListNode* pNext = NULL;
        while(pCur!=NULL)
        {
            if(pCur->next!=NULL && pCur->value == pCur->next->value)
            {
                pNext = pCur->next;
                while(pNext->next!=NULL && pNext->value == pNext->next->value)
                    pNext = pNext->next;
                / 如果pCur指向链表中第一个元素，pCur -> ... -> pNext ->...
                // 要删除pCur到pNext, 将指向链表第一个元素的指针pHead指向pNext->next
                if(pCur == pHead)
                    pHead = pNext->next;
                // 如果pCur不指向链表中第一个元素，pPre -> pCur ->...->pNext ->...
                // 要删除pCur到pNext，即pPre->next = pNext->next
                else
                    pPre->next = pNext->next;
                // 向前移动
                pCur = pNext->next; （注意！）
            }
            else{
                pPre = pCur; // pPre移到当前位置，当前位置的指针再往下移
                pCur = pCur->next; //注意！
            }
        }
        return pHead;
    }
}