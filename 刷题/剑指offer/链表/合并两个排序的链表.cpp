ListNode* Merge(ListNode* pHead1, ListNode* pHead2)
{
    if(pHead1 == NULL)
        return pHead2;
    else if(pHead2 ==NULL)
        return pHead1;
    ListNode* merge=NULL; // merge=NULL
    if(pHead1->m_pValue < pHead2->m_pValue)
    {
        merge = pHead1;
        merge->m_pNext = Merge(pHead1->m_pNext, pHead2)
    }
    else
    {
        merge = pHead2;
        merge->m_pNext = Merge(pHead1, pHead2->m_pNext);
    }
    return merge;
}