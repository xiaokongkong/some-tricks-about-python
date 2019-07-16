# 严蔚敏版
def quick_sort(array, l, r):
    if l < r:
        q = partition(array, l, r)
        quick_sort(array, l, q - 1)
        quick_sort(array, q + 1, r)

def partition(array, l, r):
    # 一趟排序过程
    key = array[l]
    while l < r:
        while l < r and array[r] >= key:  # 移动右指针，直到找到比key小的元素
            r -= 1
        array[l] = array[r]
        while l < r and array[l] <= key:  # 移动左指针，直到找到比key大的元素
            l += 1
        array[r] = array[l]

    array[l] = key  // 这里用array[r]=key也可以，因为l和r最后会指向同一个元素
    return l
array = [54,26,93,17,77,31,44,55,20]
quick_sort(array, 0, len(array)-1)
print(array)


def quicksort(nums):
    if len(nums) <= 1:
        return nums

    # 左子数组
    left = []
    # 右子数组
    right = []
    # 基准数
    base = nums.pop()

    # 对原数组进行划分
    for x in nums:
        if x < base:
            left.append(x)
        else:
            right.append(x)

    # 递归调用
    return quicksort(left) + [base] + quicksort(right)

def main():
    nums = [6,1,2,7,9,3,4,5,10,8]
    print(quicksort(nums))

main()