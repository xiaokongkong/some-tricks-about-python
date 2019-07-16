# 任何一个数字异或它自己都等于0
# 要求：数组中除了两个只出现一次的数字外，其他数字都出现了两遍
# 思路: 按位异或，在得到的值中找到二进制最后一个1，然后把数组按照该位是0还是1分为两组
def get_only_one_number(nums):
    if not nums:
        return None
    tmp_ret = 0
    for n in nums:  # 获取两个值的异或结果
        tmp_ret ^= n
    last_one = get_bin(tmp_ret)
    a_ret, b_ret = 0, 0  # 分成两组
    for n in nums:
        if is_one(n, last_one):
            a_ret ^= n  # a_ret保存第n位为1的数字
        else:
            b_ret ^= n  # b_ret保存第n位为0的数字
    return [a_ret, b_ret]


def get_bin(num):
    # 在整数num的二进制中找到最右边是1的位
    ret = 0
    while num & 1 == 0 and ret < 32:
        num = num >> 1
        ret += 1
    return ret


def is_one(num, t):
    # 判断在num的二进制表示中，从右数起的t位是不是1
    num = num >> t
    return num & 1



