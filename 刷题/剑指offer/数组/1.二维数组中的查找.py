# 递归
class Solution:
    # array 二维列表
    def Find(self, target, array):
        if len(array) == 0:
            return False
        for i, row in enumerate(array):  # 遍历行
            for j, item in enumerate(row):  # 遍历列
                if item == target:
                    return True
                elif item > target:
                    array = [x[:j] for x in array[i + 1:]]
                    return self.Find(target, array)


# 非递归
class Solution_:
    # array 二维列表
    def Find(self, target, array): 
        # 非递归
        m = len(array) # 行数
        n = len(array[0]) - 1 # 列数减1
        i = 0
        while i < m and n >= 0:
            if target > array[i][n]:  # 行数加一，往下移动
                i += 1
            elif target < array[i][n]: # 列数减一，往左移动
                n -= 1
            else:
                return True
        return False    