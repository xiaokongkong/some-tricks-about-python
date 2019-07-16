# 广度优先搜索,按层次遍历
# C++
void PrintFromTopToBottom(BinaryTreeNode* pTreeRoot)
{
    if(!pTreeRoot)
        return;
    std::deque<BinaryTreeNode *>dequeTreeNode;
    dequeTreeNode.push_back(pTreeRoot); //add the element at the end
    while(dequeTreeNode.size())
    {
        BinaryTreeNode *pNode = dequeTreeNode.front(); // 获取第一个元素
        dequeTreeNode.pop_front(); //删除第一个元素

        printf("%d ",pNode->m_pValue); //打印

        if(pNode->m_pLeft) //左结点存在，就把左结点放入队列
            dequeTreeNode.push_back(pNode->m_pLeft);
        if(pNode->m_pRight) //右结点存在，就把右结点放入队列
            dequeTreeNode.push_back(pNode->m_pRight);
    }
}

# python
def bfs(tree):
    if not tree:
        return None
    stack = [tree]  # 树的头结点（一个结点）
    ret = []
    while stack:
        node = stack.pop(0)
        ret.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return ret