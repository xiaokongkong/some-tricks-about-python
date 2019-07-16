# 有右子树，next就是它的右子树的最左结点
# 无右子树，是父结点的左子结点，next就是父节点
# 无右子树，是父结点的右子结点，需要沿着指向父结点的指针向上遍历，直到找到一个是它父结点的左子结点的结点，
# next是这个结点的父结点

BinaryTreeNode* GetNext(BinaryTreeNode* pNode)
{
    if(pNode == NULL)
        return NULL;
    BinaryTreeNode* pNext = NULL;

    // 有右子树
    if(pNode->m_pRight!=NULL)
    {
        BinaryTreeNode* pRight = pNode->m_pRight；
        while(pRight->m_pLeft!=NULL)
            pRight = pRight->m_pLeft;
        pNext = pRight;
    }
    // 无右子树，且父结点不为空
    else if(pNode->m_Parent!=NULL)
    {
        BinaryTreeNode* pCurrent = pNode;  // 当前结点
        BinaryTreeNode* pParent = pNode->parent;  // 父结点
        // 当处于第三种情况的时候，才会进入这个循环
        // 直到pParent=NULL或当前结点是父结点的左子结点时，停止循环
        while(pParent!=NULL && pCurrent == pParent->m_pRight)
        {
            pCurrent = pParent;
            pParent = pParent->m_pParent;
        }
        // 第二种情况，由于不满足循环条件，会直接跳到这一步
        pNext = pParent;
    }
}