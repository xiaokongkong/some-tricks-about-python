def mergeSort(alist):
    if len(alist) <= 1:
        return alist
    mid = len(alist) // 2

    left = mergeSort(alist[:mid])
    right = mergeSort(alist[mid:])
    print('left:', left)
    print('right:', right)
    return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):  # 两个指针同步移动
        if left[i] <= right[j]:
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1
    # 下面两条语句中，只有一个会执行
    result += left[i:]  # 若第一个表未检测完，添加到result后面
    result += right[j:]  # 若第二个表未检测完，添加到result后面
    return result


seq = [5, 3, 0, 6, 1, 4]
print('排序前：', seq)
result = mergeSort(seq)
print('排序后：', result)