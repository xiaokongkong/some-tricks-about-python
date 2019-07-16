class Solution{
public:
    TreeNode* Convert(TreeNode* pRootOfTree)
    {
        if(pRootOfTree == nullptr)
            return nullptr;
        TreeNode* pre = nullptr;
        convertHelper(pRootOfTree, pre);
        TreeNode* res = pRootOfTree;
        // res等于根结点，但是双向链表的头结点是最左边的结点，
        // 所以需要遍历到最左边，把最左边的结点设为头结点
        while(res -> left)  // 当还有左子树的时候，就一直往左边走
            res = res ->left;
        return res;
    }
    void convertHelper(TreeNode* cur,TreeNode*& pre) //*& ？
    {
        if(cur == nullptr)
            return;
        convertHelper(cur->left, pre);  // 一直往左，直到cur=nullptr,查看当前结点有没有右子树，再进行遍历
        cur->left = pre;  // cur和pre互指，cur->left = pre，pre->right = cur
        if(pre)
            pre->right = cur;
        pre = cur;  // 然后把pre更新为cur
        convertHelper(cur->right, pre);
    }
}