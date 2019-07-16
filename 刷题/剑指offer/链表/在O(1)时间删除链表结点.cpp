// 我们把下一个结点的内容复制到需要删除的结点上，覆盖原内容，
// 再把下一个结点删除，就相当于把当前结点删除了

void DeleteNode(ListNode** pListHead, ListNode* pToBeDeleted)
{
    if(!pListHead || !pToBeDeleted)
        return;

    // 要删除的结点不是尾结点
    if(pToBeDeleted->m_pNext!=NULL)
    {
        ListNode* pNext = pToBeDeleted -> m_pNext;  // 找到下一个结点
        pToBeDeleted -> m_pVal = pNext -> m_pVal;  // 把下一个结点的内容复制到需要删除的结点上
        pToBeDeleted -> m_pNext = pNext -> m_pNext; // 当前结点的next指向下下一个结点

        delete pNext;  // 删除下一个结点
        pNext = NULL;
    }
    else if(*pListHead == pToBeDeleted) // 链表只有一个结点，删除头结点（也是尾结点）
    {
        delete pToBeDeleted;
        pToBeDeleted = NULL;
        *pListHead = NULL;
    }
    else //当删除的是尾结点
    {
        ListNode* pNode = *pListHead;  // 创建的是 *pListHead 结点（带*号的）
        while(pNode -> m_pNext != pToBeDeleted) // pNode->m_pNext=pToBeDeleted
        {
            pNode = pNode -> m_pNext;
        }
        pNode -> m_pNext = NULL;
        delete pToBeDeleted;
        pToBeDeleted = NULL;
    }

}