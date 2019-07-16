# 第一个指针初始化时指向数组的第一个数字，它只向后移动；
# 第二个指针初始化时指向数组的最后一个数字，它只向前移动；
# 在两个指针相遇前，第一个指针总是位于第二个指针前面。
# 如果第一个指针指向的是偶数，并且第二个指针指向的数字是奇数，我们就交换这两个数字
def record(nums, is_even):
    left, right = 0, len(nums) - 1  # left用来判断偶数，right用来判断奇数
    while left < right:
        while not is_even(left):  # 循环直到找到偶数
            left += 1
        while is_even(right):  # 循环直到找到奇数
            right -= 1
        if left < right:
            nums[left], nums[right] = nums[right], nums[left]


def is_even(num):
    return (num & 1) == 0
