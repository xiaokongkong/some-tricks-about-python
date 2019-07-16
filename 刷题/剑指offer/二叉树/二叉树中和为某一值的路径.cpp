class Solution {
public:
    vector<vector<int> > FindPath(TreeNode* root,int expectNumber) {

        vector<vector<int> > res;
        vector<int> path;
        if (root == nullptr)
            return res;

        Search(root, expectNumber, res, path);
        return res;
    }


    void Search(TreeNode *root,int expectNumber, vector<vector<int> > &res, vector<int> &path)
    {
        if(root->left==nullptr && root->right==nullptr)
        {
            if(root->val==expectNumber)  # 找到一条路径，path中存入，res中保存path，然后path再弹出
            {
                path.push_back(root->val);
                res.push_back(path);
                path.pop_back();
            }
            return;
        }
        path.push_back(root->val); # root->left或 root->right不为空
        if(root->left)
            Search(root->left,expectNumber - root->val, res,path);
        if(root->right)
            Search(root->right,expectNumber - root->val,res,path);
        path.pop_back();
    }
};