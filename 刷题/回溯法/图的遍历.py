'''
图的遍历

从一个节点出发，不重复地经过所有其它节点后，回到出发节点。找出所有的路径
从图中的一个节点E出发，不重复地经过所有其它节点后，回到出发节点E，称为一条路径。请找出所有可能的路径。
'''

# 用邻接表表示图
n = 6
a, b, c, d, e, f = range(n)
graph = [
    {b, c},
    {c, d, e},
    {a, d},
    {c},
    {f},
    {c, d}
]
x = [0] * (n + 1)
X = []


def conflict(k):
    global n, graph, x
    # 第k个节点，是否前面已经走过
    if k < n and x[k] in x[:k]:  # x[k] in x[:k]此节点在前面出现果
        return True
    # 回到出发节点
    if k == n and x[k] != x[0]:  # 一条路径走完
        return True
    return False


# 图的遍历
def dfs(k):
    global n, a, b, c, d, e, f, graph, x, X
    # 解的长度超出，已走遍n+1个节点 （若不回到出发节点，则 k==n）
    if k > n:
        print(x)
    else:
        # 遍历节点x[k]的邻接节点（x[k]的所有状态）
        for node in graph[x[k - 1]]:
            x[k] = node
            print(x)
            if not conflict(k):  # 剪枝
                dfs(k + 1)


x[0] = a  # 出发节点
print(x)
dfs(1)  # 开始处理解x中的第2个节点。这里是1!!
