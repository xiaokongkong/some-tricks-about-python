def get_first_k(data,length,k,start,end):
    if start>end:
        return -1
    mid_index = (start + end) // 2  # 这里是 start+end
    mid_data = data[mid_index]
    if mid_data == k:
        if (mid_index>0 and data[mid_index-1]!=k) or mid_index == 0:
            return mid_index
        else:
            end = mid_index - 1
    elif mid_data < k:
        start = mid_index + 1
    else:
        end = mid_index - 1
    return get_first_k(data, length, k, start, end)


def get_last_k(data, length, k, start, end):
    if start > end:
        return -1
    mid_index = (start + end) // 2
    mid_data = data[mid_index]
    if mid_data == k:
        if mid_index == 0 or (mid_index < length-1 and data[mid_index+1]!=k):
            return mid_index
    elif mid_data < k: # k在右半部分
        start = mid_index + 1
    else:  # k在左半部分
        end = mid_index - 1
    return get_last_k(data, length, k, start, end)

def get_number_of_k(data, length, k):
    number = 0
    if data and length>0:
        first_k = get_first_k(data, length, k, 0, length-1)
        last_k = get_last_k(data, length, k, 0, length-1)
    if first_k > -1 and last_k > -1:
        number = last_k - first_k +1
    return number


# 非递归
def get_k_counts(nums, k):
    first = get_first_k(nums, k)
    last = get_last_k(nums, k)
    if first < 0 and last < 0:
        return 0
    if first < 0 or last < 0:
        return 1
    return last - first + 1


def get_first_k(nums, k):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < k:
            if mid + 1 < len(nums) and nums[mid + 1] == k:
                return mid + 1
            left = mid + 1
        elif nums[mid] == k:
            if mid - 1 < 0 or (mid - 1 >= 0 and nums[mid - 1] < k):
                return mid
            right = mid - 1
        else:
            right = mid - 1
    return -1


def get_last_k(nums, k):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < k:
            left = mid + 1
        elif nums[mid] == k:
            if mid + 1 == len(nums) or (mid + 1 < len(nums) and nums[mid + 1] > k):
                return mid
            left = mid + 1
        else:
            if mid - 1 >= 0 and nums[mid - 1] == k:
                return mid - 1
            right = mid - 1
    return -1

# 直接调用count计算
class Solution:
    def GetNumberOfK1(self, data, k):
        if len(data) == 0:
            return 0
        else:
            return data.count(k)
