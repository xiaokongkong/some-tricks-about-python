# 要求：在一个数组中，前面的数字比后面的大，就是一个逆序对，求总数
# 思路: 归并排序,先把数组依次拆开，然后合并的时候统计逆序对数目，并排序
# 算法的流程和书上一致，l_right, r_right分别是两个指针
import copy


def get_inverse_pairs(nums):
    if not nums:
        return 0
    start, end = 0, len(nums) - 1
    tmp = copy.deepcopy(nums)
    return inverse_pairs(tmp, start, end)


def inverse_pairs(tmp, start, end):
    # print(tmp,start,end)
    if start == end:  # 递归结束条件
        return 0
    mid = (end - start) // 2
    left = inverse_pairs(tmp, start, start + mid)  # 左边的逆序对数
    right = inverse_pairs(tmp, start + mid + 1, end)  # 右边的逆序对数
    count = 0  # 本次逆序对数目
    l_right, r_right = start + mid, end
    t = []  # 保存排序结果，是从大到小的
    while l_right >= start and r_right >= start + mid + 1:
        if tmp[l_right] > tmp[r_right]:
            t.append(tmp[l_right])  # 这一步决定了tmp是从大到小的
            count += (r_right - mid - start)
            l_right -= 1
        else:
            t.append(tmp[r_right])
            r_right -= 1

    while l_right >= start:
        t.append(tmp[l_right])
        l_right -= 1

    while r_right >= start + mid + 1:
        t.append(tmp[r_right])
        r_right -= 1
    tmp[start:end + 1] = t[::-1]

    return count + left + right


print(get_inverse_pairs([7, 5, 6, 4]))