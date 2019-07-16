class Solution {
public:
    TreeNode* R(<vector<int> a, int abegin,int aend, vector<int> b,int bbegin,int bend)
    {
        if(abegin>=aend || bbegin>=bend)
            return NULL;
        TreeNode* root=new TreeNode(a[abegin]);
        int pivot;  //在中序序列中找到root所在的位置
        for(pivot=bbegin;pivot<bend;pivot++)
            if(b[pivot]==a[abegin])
                break;
        root->left=R(a,abegin+1,abegin+pivot-bbegin+1,b,bbegin,pivot);
        //left: [abegin+1, abegin+pivot-bbegin+1)  最后的加1，是取不到的
        //      [bbegin, pivot)
        root->right=R(a,abegin+pivot-bbegin+1,aend,b,pivot,bend);
        //right: [abegin+pivot-bbegin+1,aend)
        //       [pivot, bend)
        return root;
        
    }


    TreeNode* reConstructBinaryTree(vector<int> pre,vector<int> vin) {
        return R(pre,0,pre.size(),vin,0,vin.size());  //因为起始从0开始，所以是一个左闭右开的区间
    }
};