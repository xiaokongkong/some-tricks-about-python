'''
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

示例 1 :

输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
说明 :

数组的长度为 [1, 20,000]。
数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subarray-sum-equals-k
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# 前缀和 + 哈希
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) == 0:
            return 0
        result, cur_sum = 0, 0
        sum_dict = {0: 1}
        for num in nums:
            cur_sum += num # cur_sum等于原先的cur_sum加上当前的num
            result += sum_dict.get(cur_sum - k, 0)  # 找到cur-k对应的个数
            sum_dict[cur_sum] = sum_dict.get(cur_sum, 0) + 1 # 把当前和加入sum_dict中

        return result


'''
class Solution {
public:
  int subarraySum(vector<int>& nums, int k) {
    if (nums.empty()) 
        return 0;
    unordered_map<int, int> counts{{0,1}};
    int cur_sum = 0;
    int ans = 0;
    for (const int num : nums) {
      cur_sum += num;      
      ans += counts[cur_sum - k];
      ++counts[cur_sum];
    }
    return ans;
  }
};
'''