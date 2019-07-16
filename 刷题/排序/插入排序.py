def insertionSort(alist):
    for index in range(1, len(alist)):
        currentvalue = alist[index] # 保存当前值
        position = index
        while position > 0 and alist[position - 1] > currentvalue:
            # 如果前一个值比当前值大，就把当前值往前移
            alist[position] = alist[position - 1]
            position = position - 1
        alist[position] = currentvalue
