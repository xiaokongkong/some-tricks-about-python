
'''
遍历子集树，时间复杂度 O(2^n)

如果解的长度是不固定的，那么解和元素顺序无关，即可以从中选择0个或多个。例如：子集，迷宫，...

如果解的长度是固定的，那么解和元素顺序有关，即每个元素有一个对应的状态。例如：子集，8皇后，...

解空间的个数指数级别的，为2^n,可以用子集树来表示所有的解

适用于：幂集、子集和、0-1背包、装载、8皇后、迷宫、...

'''


n = 4
a = [1, 2, 3, 4]
x = []
X = []

import pysnooper


# 冲突检测：无
@pysnooper.snoop()
def conflict(k):
    global n, x, X, a
    return False  # 无冲突

# 一个例子
# 冲突检测：奇偶性相同，且和小于8的子集
@pysnooper.snoop()
def conflict2(k):
    global n, x, X, a
    if k == 0:
        return False

    # 根据部分解，构造部分集
    s = [y[0] for y in filter(lambda s: s[1] != 0, zip(a[:k + 1], x[:k + 1]))]
    print(s)
    if len(s) == 0:
        return False
    if 0 < sum(map(lambda y: y % 2, s)) < len(s) or sum(s) >= 8: # 只比较 x[k] 与 x[k-1] 奇偶是否相间
        return True

    return False  # 无冲突

# 子集树递归模板
@pysnooper.snoop()
def subsets(k):  # 到达第k个元素
    global n, x, X
    print(x)
    if k >= n:  # 超出最尾的元素
        X.append(x[:])  # 保存（一个解）
    else:
        for i in [1, 0]:  # 遍历元素 a[k] 的两种选择状态:1-选择，0-不选
            x.append(i)
            if not conflict2(k):  # 剪枝  # 如果不矛盾的话，就继续往下走，如果矛盾，就剪枝（x.pop()）
                subsets(k + 1)
            x.pop()  # 回溯

# 根据一个解x，构造一个子集
@pysnooper.snoop()
def get_a_subset(x):
    global a
    return [y[0] for y in filter(lambda s: s[1] != 0, zip(a, x))]

# 根据一组解X, 构造一组子集
@pysnooper.snoop()
def get_all_subset(X):
    return [get_a_subset(x) for x in X]


subsets(0)
print("x:", x)
print("X:", X)

print(get_all_subset(X))

'''
X: [[1, 0, 1, 0], [1, 0, 0, 0], [0, 1, 0, 1], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [0, 0, 0, 0]]
对应的是
[[1, 3], [1], [2, 4], [2], [3], [4], []]

如果subsets(k)中改为for i in [1,0]，那么结果的顺序是反过来的
X: [[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0], [1, 0, 1, 0]]
对应的是
[[], [4], [3], [2], [2, 4], [1], [1, 3]]


X中的每个值都是x，相当于是从1（第一个数）开始，而且conflict2为false的话（不矛盾），那么就采用这一步，然后继续下去，直到满足k>=n，就回溯；
就是选它和不选它，两种情况，然后这两种情况又分别继续下去，去判断，是否为一个子集
'''


'''
回溯法的子集树模板

'''
void backtrack(int t)
{
    if(t>n)
        output(x);
    else
        for(int i=0;i<=1;i++)
        {
            x[t]=i;
            if(constraint(t) && bound(t))
                backtrack(t+1);
        }
}


'''
回溯法搜索排列树
'''
void backtrack(int t)
{
    if(t>n)
        output(x);
    else
        for(int i=t;i<n;i++)
        {
            swap(x[t],x[i]);
            if(constraint(t) && bound(t))
                backtrack(t+1);
            swap(x[t],x[i]);
        }
}