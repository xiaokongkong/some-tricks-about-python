def MAX_Heapify(heap, HeapSize, root):  # 在堆中做结构调整使得父节点的值大于子节点
    left = 2 * root + 1
    right = left + 1
    larger = root
    if left < HeapSize and heap[larger] < heap[left]:
        larger = left  # 找到root和left之间的最大值x
    if right < HeapSize and heap[larger] < heap[right]:
        larger = right  # 把right和刚才的最大值x比较
    if larger != root:  # 如果最大值不是root,就要进行调整
        # 如果做了堆调整则larger的值等于左节点或者右节点的，这个时候做交换操作
        heap[larger], heap[root] = heap[root], heap[larger]
        MAX_Heapify(heap, HeapSize, larger)  # 重新调整，退出的条件是，root>=left且root>=right


def Build_MAX_Heap(heap):  # 构造一个堆，将堆中所有数据重新排序
    HeapSize = len(heap)  # 将堆的长度单独拿出来
    for i in range((HeapSize - 2) // 2, -1, -1):  # 从后往前数
        MAX_Heapify(heap, HeapSize, i)  # 重新调整


def HeapSort(heap):
    # 将根节点取出与最后一位做对调，对前面len-1个节点继续进行对调整过程。
    Build_MAX_Heap(heap)  # 构建一个大根堆
    for i in range(len(heap) - 1, -1, -1):
        # i的取值范围是7-0，每次0都是最大的，然后分别和7->0等7个元素进行交换
        heap[0], heap[i] = heap[i], heap[0]
        MAX_Heapify(heap, i, 0)  # 重新调整,这里的i是size,依次是7、6、5直到0，表示要重新调整的节点数
    return heap


a = [53, 17, 78, 9, 45, 65, 87, 32]
HeapSort(a)
print(a)
