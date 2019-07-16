void Print(BinaryTreeNode* pRoot)
{
    if(pRoot == NULL)
        return;
    std::stack<BinaryTreeNode*> levels[2];
    int current=0;
    int next=1;
    levels[current].push(pRoot);
    while(!levels[0].empty() || !levels[1].empty())
    {
        BinaryTreeNode* pNode = levels[current].top(); // 取出栈顶元素
        levels[current].pop() // 弹出栈顶元素
        print("%d ", pNode->value);

        if(current == 0) // 奇数层，从左到右
        {
            if(pNode->left != NULL)
                levels[next].push(pNode->left);
            if(pNode->right != NULL)
                levels[next].push(pNode->right);
        }
        else  // 偶数层，从右到左
        {
            if(pNode->right != NULL)
                levels[next].push(pNode->right);
            if(pNode->left != NULL)
                levels[next].push(pNode->left);
        }

        if(levels[current].empty()) // 一层遍历完毕
        {
            print("\n");
            current = 1 - current;  //current和next是对立的，只能是0-1或1-0
            next = 1 - next;  //
        }

    }
}