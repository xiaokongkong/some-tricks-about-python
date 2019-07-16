ListNode* ReverseList(ListNode* pHead)
{
    ListNode* pReversed = NULL;
    ListNode* pNode = pHead;
    ListNode* pPrev = NULL;

    while(pNode != NULL) // 这里是while
    {
        ListNode* pNext = pNode -> m_pNext;
        if(pNext==NULL) // 这里是if 和 pNext
        {
            pReversed = pNode;
        }
        pNode -> m_pNext = pPrev;
        pPrev = pNode;
        pNode = pNext;
    }
    return pReversed;
}