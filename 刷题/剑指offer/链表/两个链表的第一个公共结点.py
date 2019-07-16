#https://cuijiahua.com/blog/2018/01/basis_36.html
# 把第一个链表拼在第二个链表后面
# 把第二个链表拼在第一个链表后面
# 这样就生成了两个同样长度的链表，然后同时遍历这两个表，就可以找到共结点
# 原理：
# 假设第一个是3+5（公共的部分长度是5），第二个是2+5
# 3+5+2 == 2+5+3，然后从11开始，就是公共部分
# 时间复杂度O(m+n)，空间复杂度O(m+n)
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        if pHead1 == None or pHead2 ==None:
            return None
        cur1, cur2 = pHead1, pHead2
        while cur1 != cur2:
            cur1 = cur1.next if cur1!=None else pHead2
            cur2 = cur2.next if cur2!=None else pHead1
        return cur1
