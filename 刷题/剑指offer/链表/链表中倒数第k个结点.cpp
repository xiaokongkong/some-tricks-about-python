ListNode* FindKthToTail(ListNode* pListHead, unsigned int k)
{
    ListNode* pAhead = pListHead;
    ListNode* pBehind = NULL;
    for(unsigned int i=0; i<k-1;i++)  // 这里是k-1
    {
        pAhead = pAhead -> m_pNext;
    }
    pBehind = pListHead;
    while(pAhead -> m_pNext!=NULL)
    {
        pAhead = pAhead -> m_pNext;
        pBehind = pBehind -> m_pNext;
    }
    return pBehind;
}