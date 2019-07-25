'''
问题
有面额10元、5元、2元、1元的硬币，数量分别为3个、5个、7个、12个。现在需要给顾客找零16元，要求硬币的个数最少，应该如何找零？或者指出该问题无解。

分析
元素——状态空间分析大法：四种面额的硬币看作4个元素，对应的数目看作各自的状态空间，遍历状态空间，其它的事情交给剪枝函数。

解的长度固定：4

解的编码：(x1,x2,x3,x4) 其中x1∈[0,1,2,3], x2∈[0,1,2,3,4,5], x3∈[0,1,2,...,7], x4∈[0,1,2,...,12]

求最优解，增添全局变量：best_x, best_num

套用回溯法子集树模板。
'''

'''找零问题'''

'''
解的长度固定：4
'''

n = 4
a = [10, 5, 2, 1]  # 四种面额
b = [3, 5, 7, 12]  # 对应的硬币数目（状态空间）

m = 53  # 给定的金额

x = [0] * n  # 一个解（n元0-b[k]数组）
X = []  # 一组解

best_x = []  # 最佳解
best_num = 0  # 最少硬币数目


def conflict(k):
    global n, m, x, X, a, b, best_num
    # 部分解的金额已超
    if sum([p * q for p, q in zip(a[:k + 1], x[:k + 1])]) > m:
        return True

    # 部分解的金额加上剩下的所有金额不够
    if sum([p * q for p, q in zip(a[:k + 1], x[:k + 1])]) + sum([p * q for p, q in zip(a[k + 1:], b[k + 1:])]) < m:
        return True

    # 部分解的硬币个数超best_num
    num = sum(x[:k + 1])
    if 0 < best_num < num:
        return True
    return False  # 无冲突


def subsets(k): # 到达第k个元素
    global n, a, b, x, X, best_x, best_num
    if k == n:  # 超出最尾的元素
        X.append(x[:])  # 保存（一个解）
        # 计算硬币数目，若最佳，则保存
        num = sum(x)
        if best_num == 0 or best_num > num:
            best_num = num
            best_x = x[:]
    else:
        for i in range(b[k] + 1):  # 遍历元素 a[k] 的可供选择状态: 0, 1, 2, ..., b[k] 个硬币
            x[k] = i
            if not conflict(k):  # 剪枝
                subsets(k + 1)


subsets(0)
print(best_x)
