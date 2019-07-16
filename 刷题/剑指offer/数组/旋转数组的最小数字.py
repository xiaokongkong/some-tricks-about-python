def find_min(nums):
    if not nums:
        return False
    length = len(nums)
    left, right = 0, length - 1  # 两个指针
    while nums[left] >= nums[right]:
        if right - left == 1:
            return nums[right]
        mid = (left + right) // 2
        if nums[left] == nums[right] == nums[mid]:  # 出现重复数字
            return min(nums)
        if nums[left] <= nums[mid]:
            # 中间元素大于最左边的数，说明中间元素出现在左边的递增序列中 [3,4,5,6,7,1,2]
            left = mid
        if nums[right] >= nums[mid]:
            # 中间元素小于最右边的数，说明中间元素出现在右边的递增序列中 [6,7,1,2,3,4,5]
            right = mid
    return nums[0]  # nums[left] < nums[right],说明本身就是从小到大的
