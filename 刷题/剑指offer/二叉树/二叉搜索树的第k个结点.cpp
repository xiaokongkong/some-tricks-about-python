# 给定一棵二叉搜索树，请找出其中第k大的结点
# 思路：中序遍历的第k个结点
BinaryTreeNode* KthNode(BinaryTreeNode* pRoot, unsigned int k)
{
    if(pRoot == NULL || k == 0)
        return NULL;
    return KthNodeCore(pRoot, k);
}
BinaryTreeNode* KthNodeCore(BinaryTreeNode* pRoot, unsigned int& k)
{
    BinaryTreeNode* target = NULL;
    // 先遍历左结点
    if(pRoot->left != NULL)
    {
        target = KthNodeCore(pRoot->left, k);
    }
    // 如果没有找到target，则继续减小k，如果k等于1，说明到了第k大的数
    if(target == NULL)
    {
        if(k == 1)
            target = pRoot;
        k--;
    }
     // 如果没有找到target，继续找右结点
    if(target == NULL && pRoot->right != NULL)
        target = KthNodeCore(pRoot->right, k);

    return target;
}
