// 序列化
# 前序遍历二叉树，把空的地方都写作$
void Serialize(BinaryTreeNode* pRoot, ostream& stream)
{
    if(pRoot = NULL)
    {
        strerm << "$,";
        return;
    }
    stream << pRoot->value<<',';
    Serialize(pRoot->left, stream);
    Serialize(pRoot->right, stream);
}

void Deserialize(BinaryTreeNode** pRoot, ostream& stream)
{
    int number;
    if(ReadStream(stream, &number))
    {
        *pRoot = new BinaryTreeNode();
        (*pRoot)->value = number;
        (*pRoot)->left = NULL;
        (*pRoot)->right = NULL;

        Deserialize(&((*pRoot)->left), stream);
        Deserialize(&((*pRoot)->right), stream);
    }
}