void Print(BinaryTreeNode* pRoot)
{
    if(pRoot == NULL)
        return NULL;
    std::queue<BinaryTreeNode*> nodes;
    nodes.push(pRoot);
    int nextLevel = 0;
    int toBePrinted = 1;
    while(!nodes.empty)
    {
        BinaryTreeNode* pNode = nodes.front(); // 第一个元素
        print("%d ", pNode->value);

        if(pNode->left != NULL)
        {
            nodes.push(pNode->left);
            ++nextLevel;
        }
        if(pNode->right != NULL)
        {
            nodes.push(pNode->right);
            ++nextLevel;
        }
        nodes.pop();
        --toBePrinted;
        if(toBePrinted == 0)  //当前层打印完
        {
            print('\n');
            toBePrinted = nextLevel; // nextLevel代表的是下一层的结点数
            nextLevel = 0;  //置为0，开始重新统计
        }
    }
}