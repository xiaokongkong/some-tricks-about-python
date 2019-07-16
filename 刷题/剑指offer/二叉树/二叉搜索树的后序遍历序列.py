# 题目：输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
# 如果是则输出True否则输出False。假设输入的数组的任意两个数字都互不相同。
# 思路：
# 1、判断输入为空、二叉树只有左子树、二叉树只有右子树的情况
# 2、使用index分割左右子树
# 3、使用递归判断左右子树是否为后序遍历

class Solution:
    def VerifySequenceOfBST(self, sequence):
        if len(sequence) <= 0:
            return False
        root = sequence[-1]
        length = len(sequence)
        if min(sequence) > root or max(sequence) < root:
            # min(sequence)>root 只有右子树
            # max(sequence)<root 只有左子树
            return True
        index = 0
        for i in range(length - 1):  # 用index分割左右子树
            index = i
            if sequence[i] > root:  # 直到找到比root大的值，此时已经到右子树的部分了
                break
        for j in range(index + 1, length):  # 沿用刚才的index
            if sequence[j] < root:  # 如果在右子树中出现比root小的树，则不是一个二叉搜索树
                return False
        left = True
        right = True
        if index > 0:  # 存在左子树，递归左子树
            left = self.VerifySequenceOfBST(sequence[:index])  # index是左子树的根结点
        if index < length - 1:  # 存在右子树，递归右子树
            right = self.VerifySequenceOfBST(sequence[index:length - 1])  # index是右子树的根结点
        return left & right  # 只有当左右子树都为后序遍历时，结果为后序遍历
