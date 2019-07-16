# 在一个长度为n的数组里的所有数字都在0到n~1的范围内。
# 数组中某些数字是重复的，但不知道有几个数字重复了，
# 也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。
# 例如，如果输入长度为7的数组{2,3,1,0,2,5,3},那么对应的输出是重复的数字2或3.
def duplicate(nums):
    if not nums:  # 如果nums为空，返回false
        return False
    # 如果nums里的值不在0~n-1这个范围内，返回false
    for item in range(nums):
        if nums[item] < 0 or nums[item] > len(nums) - 1:
            return False

    for i, m in enumerate(nums):
        if m == i:  # 当前值等于下标，继续
            pass
        else:  # 当前值不等于下标，那么当前值应该出现在nums[m]那里
            if m == nums[m]:  # 当前值m和nums中以m为下标的值相等
                return m  # 找到重复值
            else:  # 当前值m和nums中以m为下标的值不等，进行交换
                nums[m], nums[i] = nums[i], nums[m]


nums = [2, 3, 1, 0, 2, 5, 3]
print(duplicate(nums))                             