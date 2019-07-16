def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                alist[i],alist[i+1]=alist[i+1],alist[i]
alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)


# 等同于上面的冒泡排序
def bubbleSort(alist):
    passnum = len(alist) - 1
    while passnum > 0:
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                alist[i],alist[i+1]=alist[i+1],alist[i]
        passnum -= 1
alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)


# 与上面的冒泡排序不同的是，增加了一个exchanges，来标记是否进行交换
def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist) - 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                exchanges = True
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
        passnum = passnum - 1
