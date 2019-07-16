# 要求：只含有2、3、5因子的数是丑数，求第1500个丑数
# 思路: 按顺序保存已知的丑数，下一个是已知丑数中某三个数乘以2，3，5中的最小值
class Solution(object):
    def nthUglyNumber(self, n):
        ugly = [1]
        t2 = t3 = t5 = 0
        while len(ugly) < n:
            while ugly[t2] * 2 <= ugly[-1]:
                t2 += 1
                print('1')
            while ugly[t3] * 3 <= ugly[-1]:
                t3 += 1
                print('2')
            while ugly[t5] * 5 <= ugly[-1]:
                t5 += 1
                print('3')
            ugly.append(min(ugly[t2] * 2, ugly[t3] * 3, ugly[t5] * 5))
            # return ugly[-1]
        return ugly


def GetUglyNumber_Solution(self, index):
    if index < 1:
        return 0
    res = [1]
    t2, t3, t5 = 0, 0, 0
    while len(res) < index:
        minNum = min(res[t2], res[t3], res[t5])
        if minNum > res[-1]:
            res.append(minNum)
        if res[-1] == res[t2] * 2:
            t2 += 1
        elif res[-1] == res[t3] * 3:
            t3 += 1
        else:
            t5 += 1
    return res[-1]


x = Solution()
y = x.nthUglyNumber(10)
print(y)