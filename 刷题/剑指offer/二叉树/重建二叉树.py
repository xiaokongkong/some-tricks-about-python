# python
class Solution:
    def reConstructBinaryTree(self, pre, vin):
        if not pre or not vin:
            return None
        root = TreeNode(pre.pop(0))  # 根结点
        index = vin.index(root.val)  # 中序中根结点的位置
        root.left = self.reConstructBinaryTree(pre, vin[:index])
        root.right = self.reConstructBinaryTree(pre, vin[index + 1:])
        return root
