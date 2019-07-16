# 和为s的两个数组
# 要求：输入一个递增排序的数组和一个数字s，在数组中查找两个数，使其和为s
# 思路: 设置头尾两个指针，和大于s，尾指针减小，否砸头指针增加
def sum_to_s(nums, s):
    start, end = 0, len(nums) - 1
    while start < end:
        if nums[start] + nums[end] == s:
            return [nums[start], nums[end]]
        elif nums[start] + nums[end] > s: # 说明nums[end]大了，要把它调小
            end -= 1
        else:
            start +=1
    return None


# 和为s的连续正数序列
# 要求：输入一个正数s， 打印出所有和为s的正整数序列(至少两个数)
# 思路: 使用两个指针，和比s小，大指针后移，比s大，小指针后移
def sum_to_s(s):
    a, b = 1, 2
    ret = []
    while a < s/2+1:
        if sum(range(a, b+1)) == s:
            ret.append(range(a, b+1))
            a += 1
        elif sum(range(a, b+1)) < s:
            # 如果从small到big的序列的和小于s，
            # 我们可以增大big，让这个序列包含更多的数字
            b += 1
        else:
            # 如果从small到big的序列的和大于s，
            # 我们可以增大small，也就是从这个序列中去掉较小的值
            a += 1