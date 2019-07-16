bool isSymetrical(BinaryTreeNode* pRoot)
{
    return isSymetrical(pRoot, pRoot);
}
bool isSymetrical(BinaryTreeNode* pRoot1, BinaryTreeNode* pRoot2)
{
    if(pRoot1 == NULL && pRoot2 == NULL)
        return true;
    if(pRoot1 == NULL || pRoot2 == NULL)
        return false;
    if(pRoot1->m_nValue != pRoot2->m_nValue)
        return false;
    return isSymetrical(pRoot1->m_pLeft, pRoot2->m_pRight) &&
           isSymetrical(pRoot1->m_pRight, pRoot2->m_pLeft)