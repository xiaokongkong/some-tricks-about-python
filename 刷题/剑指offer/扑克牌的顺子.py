# 要求：从扑克牌中随机抽取5张牌，判断是不是顺子，大小王可以当任意值
# 思路: 使用排序
import random


def is_continus(nums, k):
    data = [random.choice(nums) for _ in range(k)]
    data.sort()  # 排序
    print(data)
    zero = data.count(0)  # 统计0的个数
    small, big = zero, zero + 1
    while big < k:  # k是抽出来的牌数
        if data[small] == data[big]:  # 如果存在重复数字，则不为顺子
            return False
        tmp = data[big] - data[small]  # 两个相邻的数做减法
        if tmp > 1:  # 中间有空缺
            if tmp - 1 > zero:  # 如果空缺的数量大于0的数量，则不为顺子
                return False
            else:
                zero -= tmp - 1  # 用0来补这个空缺
                small += 1  # small和big同步向后移动
                big += 1
        else:  # 如果两个数差一，就同步向后移动
            small += 1
            big += 1
    return True

