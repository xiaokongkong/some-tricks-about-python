'''
问题
从n个元素中挑选m个元素进行排列，每个元素最多可重复r次。其中m∈[2,n]，r∈[1,m]。

如：从4个元素中挑选3个元素进行排列，每个元素最多可重复r次。

分析
解x的长度是固定的，为m。

对于解x，先排第0个位置的元素x[0]，再排第1个位置的元素x[1]。我们把后者看作是前者的一种状态，即x[1]是x[0]的一种状态！！

一般地，把x[k]看作x[k-1]的状态空间a中的一种状态，我们要做的就是遍历a[k-1]的所有状态。

那么，套用子集树模板即可。
'''

n = 4
a = ['a','b','c','d']

m = 3   # 从4个中挑3个
r = 2   # 每个元素最多可重复2

x = [0]*m   # 一个解（m元0-1数组）
X = []      # 一组解

def conflict(k):
    global n,r,x,X,a
    # 部分解内的元素x[k]不能超过r
    if x[:k+1].count(x[k]) > r:
        return True
    return False # 无冲突

# 用子集树模板实现选排问题
def perm(k): # 到达第k个元素
    global n,m,a,x,X
    if k==m: # 超出最尾的元素
        print(x)
    else:
        for i in a:  # 遍历x[k-1]的状态空间a，其它的事情交给剪枝函数！
            x[k]=i
            if not conflict(k): # 剪枝
                perm(k+1)

perm(0)