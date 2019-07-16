bool hasSubTree(BinaryTreeNode* pRoot1,BinaryTreeNode* pRoot2)
{
    bool result = false;
    if(pRoot1!=NULL && pRoot2!=NULL)
    {
        if(pRoot1->m_pValue == pRoot2->m_pValue)
            result = DoesTree1HasTree2(pRoot1,pRoot2);
        if(!result)
            result = hasSubTree(pRoot1->left, pRoot2)
        if(!result)
            result = hasSubTree(pRoot1->right, pRoot2)
    }
    return result
}

bool DoesTree1HasTree2(BinaryTreeNode* pRoot1,BinaryTreeNode* pRoot2)
{
    if(pRoot1==NULL)
        return false;
    if(pRoot2==NULL)
        return true;
    if(pRoot1->m_pValue != pRoot2->m_pValue)
        return false;
    return DoesTree1HasTree2(pRoot1->left, pRoot2->left) &&
            DoesTree1HasTree2(pRoot1->right, pRoot2->right)
}