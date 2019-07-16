# 思路一: 使用heapq，该模块是一个最小堆，需要转化成最大堆，
#         只要在入堆的时候把值取反就可以转化成最大堆(仅适用于数字)
# 思路二: 数组比较小的时候可以直接使用heapq的nsmallest方法
# 利用堆
import heapq


def get_least_k_nums(nums, k):
    return heapq.nsmallest(k, nums)


class MaxHeap(object):
    def __init__(self, k):
        self.k = k
        self.data = []

    def push(self, elem):

        elem = -elem  # 入堆的时候取反，堆顶就是最大值的相反数了
        if len(self.data) < self.k:
            heapq.heappush(self.data, elem)
        else:
            least = self.data[0]
            if elem > least:
                heapq.heapreplace(self.data, elem)


def get_least_k_nums(self):
    return sorted([-x for x in self.data])




# 利用快排
def partition(array,l,r):
    key = array[l]
    while l<r:
        while l<r and array[r]>=array[key]:
            r-=1
        array[l]=array[r]
        while l<r and array[l]<=array[key]:
            l+=1
        array[r]=array[l]
    array[r]=key
    return l

def find_k_smallest(nums,k):
    length = len(nums)
    left = 0
    right = length - 1
    index = partition(nums,left,right)
    # 循环终止的条件是k==index，也就是把第k个位置上的数放好了
    # 那么在第k个位置左边的数都小于k（不一定有序）
    while k != index:
        if index > k-1: # 如果index大于k-1,那么第k个数出现在index的左边
            right = index -1
        else: # 否则,那么第k个数出现在index的右边
            left = index + 1
        index = partition(nums, left, right)
    return nums[:k]