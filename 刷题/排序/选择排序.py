'''
选择排序在冒泡排序的基础上进行了改进，每一遍扫描只需要进行一次交换。
选择排序在每一次扫描的时候，都找出最大值，并将其放在合适的位置上。
'''


def selectionSort(alist):
    for fillslot in range(len(alist) - 1, 0, -1):
        positionOfMax = 0
        # 找到最大值
        for location in range(1, fillslot + 1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location
        # 将最大值与最后一个值进行交换
        alist[fillslot], alist[positionOfMax] = alist[positionOfMax], alist[fillslot]


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selectionSort(alist)
print(alist)


def selectionSort(alist):
    fillslot = len(alist) - 1
    while fillslot > 0:
        positionOfMax = 0
        # 找到最大值
        for location in range(1, fillslot + 1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location
        # 将最大值与最后一个值进行交换
        alist[fillslot], alist[positionOfMax] = alist[positionOfMax], alist[fillslot]
        fillslot -= 1


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selectionSort(alist)
print(alist)


