# 循环
def binarySearch(alist, item):
    found = False
    first = 0
    last = len(alist) - 1
    while first <= last and not found:
        middle = (first + last) // 2
        if alist[middle] == item:
            found = True
        elif alist[middle] < item:
            last = middle - 1
        else:
            first = middle + 1
    return found


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42, ]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))


# 递归
def binarySearch(alist,item):
    if len(alist)==0: # 循环终止条件，alist内没有元素
        return False
    else:
        middle=len(alist)//2
        if alist[middle]==item: # 找到元素，返回true
            return True
        else:
            if alist[middle]>item:
                return binarySearch(alist[middle+1:],item)
            else:
                return binarySearch(alist[:middle],item)
testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))
