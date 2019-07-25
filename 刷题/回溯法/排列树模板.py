'''
遍历排列树，时间复杂度O(n!)

解空间是由n个元素的排列形成，也就是说n个元素的每一个排列都是解空间中的一个元素，那么，最后解空间的组织形式是排列树

适用于：n个元素全排列、旅行商、...
'''

'''求[1, 2, 3, 4]的全排列'''

n = 3
x = ['a','b','c']
X = []
import pysnooper


# 冲突检测：无
#@pysnooper.snoop()
def conflict(k):
    global n, x, X
    return False

# 冲突检测：元素奇偶相间的排列
#@pysnooper.snoop()
def confilct2(k):
    global n, x, X
    if k == 0:
        return False
    if x[k - 1] % 2 == x[k] % 2:
        return True
    return False


#@pysnooper.snoop()
def backkrak(k):
    global n, x, X
    if k >= n:
        print(x)
    else:
        for i in range(k, n):
            x[k], x[i] = x[i], x[k]  # swap(x[k], x[i])
            if not confilct2(k):
                backkrak(k + 1)
            x[i], x[k] = x[k], x[i]  # # swap(x[k], x[i]) 这一步不能忽略

# @pysnooper.snoop()
def backkrak_(k):
    global n, x, X
    if k >= n:
        print(x)
    else:
        for i in range(k, n):
            x[k], x[i] = x[i], x[k]
            print('before: ',x)
            backkrak_(k + 1)
            x[i], x[k] = x[k], x[i]  # 这一步不能忽略
            print('after: ',x)


backkrak_(0)
print(X, x)
