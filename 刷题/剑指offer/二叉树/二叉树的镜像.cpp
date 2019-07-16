void MirrorRecursively(BinaryTreeNode* pNode)
{
    // 判断边界
    if(pNode == NULL)
        return;
    if(pNode->m_pLeft == NULL && pNode->m_pRight == NULL)
        return;
    // 交换
    BinaryTreeNode* pTemp = pNode->m_pLeft;
    pNode->m_pLeft = pNode->m_pRight;;
    pNode->m_pRight = pTemp;
    // 对左子树和右子树进行递归
    if(pNode->m_pLeft)
        MirrorRecursively(pNode->m_pLeft);
    if(pNode->m_pRight)
        MirrorRecursively(pNode->pRight);
}