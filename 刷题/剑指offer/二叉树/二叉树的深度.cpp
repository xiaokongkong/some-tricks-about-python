# 二叉树的深度
int TreeDepth(BinaryTreeNode* pRoot)
{
    if(pRoot==NULL)
        return 0;

    int nLeft = TreeDepth(pRoot->m_pLeft);
    int nRight = TreeDepth(pRoot->m_pRight);

    return (nLeft>nRight) ? (nLeft+1):(nRight+1);
}


# 判断是否为平衡二叉树
bool IsBalanced(BinaryTreeNode* pRoot)
{
    if(pRoot==NULL)
        return ture;
    int left = TreeDepth(pRoot->m_pLeft);
    int right = TreeDepth(pRoot->m_pRight);
    int diff = left - right;
    if(diff > 1 || diff < -1)
        return false;
    return IsBalanced(pRoot->m_pLeft) && IsBalanced(pRoot->m_pRight);
}


______________________

# 判断是否为平衡二叉树
bool IsBalanced(BinaryTreeNode* pRoot, int* pDepth)
{
    if(pRoot == NULL)
    {
        pDepth = 0;
        return true;
    }
    int left,right;
    if(IsBalanced(pRoot->m_pLeft, &left) && pRoot->m_pRight, &Right))
    {
        int diff = left - right;
        if(diff <= 1 && diff >=-1)
        {
            *pDepth = 1+(left>right ? left:right);
            return ture;
        }
    }
    return false;
}
// 主函数
bool IsBalanced(BinaryTreeNode* pRoot)
{
    int depth = 0;
    return IsBalanced(pRoot, &depth);
}