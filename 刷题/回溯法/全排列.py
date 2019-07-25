'''用子集树实现全排列'''
'''
和排列树模板的区别在于，这里是把a作为原始驶入，然后新建了一个和a等长的x,用来保存结果
排列树模板中，这里的a就相当于x，然后直接修改x，并返回
'''
n = 4
a = ['a', 'b', 'c', 'd']
x = [0] * n
X = []


def conflict(k):
    global n, x, X, a
    return False  # 无冲突


def perm(k):  # 到达第k个元素
    global n, x, X, a
    if k >= n:  # 超出最尾的元素
        print(x)
    else:
        for i in set(a) - set(x[:k]):  # 遍历，剩下的未排的所有元素看作元素x[k-1]的状态空间
            x[k] = i
            if not conflict(k):  # 剪枝
                perm(k + 1)


perm(0)
