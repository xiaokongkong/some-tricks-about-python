# 长的链表先走几步，然后和短的链表一起走，直到它们俩相等
# 时间复杂度O(m+n)，空间复杂度为O(MAX(m,n))
ListNode* FindFirstCommonNode(ListNode* pHead1, ListNode* pHead2)
{
    // 得到两个链表的长度
    unsigned int nLength1 = GetListLength(pHead1);
    unsigned int nLength2 = GetListLength(pHead2);
    int nLengthDif = nLength1 -  nLength2; //length different
    ListNode* pListHeadLong = pHead1;
    ListNode* pListHeadShort = pHead2;
    if(nLength2 > nLength1)
    {
        pListHeadLong = pHead2;
        pListHeadShort = pHead1;
        nLengthDif = nLength2 -  nLength1;
    }

    // 先在长链表上走几步，再同时开始走
    for(int i = 0;i<nLengthDif;++i)
        pListHeadLong = pListHeadLong->m_pNext;

    while((pListHeadLong!=NULL) && (pListHeadShort!=NULL) && (pListHeadLong!=pListHeadShort)))
    {
        pListHeadLong = pListHeadLong ->m_pNext;
        pListHeadShort = pListHeadShort ->m_pNext;
    }

    // 得到第一个公共结点
    ListNode* pFirstCommonNOde = pListHeadLong;
    return pFirstCommonNOde;
}

unsigned int GetListLength(ListNode* pHead)
{
    unsigned int nLength = 0;
    ListNode* pNode = pHead;
    while(pNode!=NULL)
    {
        ++nLength;
        pNode = pNode->m_pNext;
    }
    return nLength;
}