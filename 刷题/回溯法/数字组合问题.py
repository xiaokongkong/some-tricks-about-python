n = 5
r = 3
a = [1, 2, 3, 4, 5]
x = [0] * n  # 一个解（n元0,1数组） 固定长度
X = []  # 一组解


def conflict(k):
    global n, r, x
    if sum(x[:k + 1]) > r:  # 部分解的长度超出r
        # 因为x里面只有0或1，所以相当于是求里面1的个数，也就是使用了几个数组
        # 此种情况为[1,1,1,1,0]
        return True
    if sum(x[:k + 1]) + (n - k - 1) < r:  # 部分解的长度加上剩下长度不够r
        # 此种情况为[0,0,0,1] 然后剩下长度只有1，所以不满足条件
        return True
    return False


def comb(k):  # 到达第k个元素
    global n, x, X
    if k >= n:  # 超出最尾的元素
        X.append(x[:])  # 保存（一个解）
    else:
        for i in [1, 0]:  # 遍历元素 a[k] 的两种选择状态:1-选择，0-不选
            x[k] = i
            if not conflict(k):  # 剪枝
                comb(k + 1)


# 根据一个解x，构造对应的一个组合
def get_a_comb(x):
    global a
    return [y[0] for y in [s for s in zip(a, x) if s[1] == 1]]


# 根据一组解X，构造对应的一组组合
def get_all_combs(X):
    return [get_a_comb(x) for x in X]


comb(0)
print(X)
print(get_all_combs(X))
