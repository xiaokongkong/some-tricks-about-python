# 思路: 使用hash，key是数字，value是出现的次数
# 注意: 列表的len方法的时间复杂度是O(1)
def get_more_half_num(nums):
    hashes = dict()
    length = len(nums)
    for n in nums:
        hashes[n] = hashes[n] + 1 if hashes.get(n) else 1
        if hashes[n] > length//2:
            return n