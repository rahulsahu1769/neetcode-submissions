class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        dic = {}
        for i in range(len(nums)):
            if target - nums[i] in dic:
                ans.append(dic.get(target-nums[i]))
                ans.append(i)
            dic[nums[i]] = i
        return ans
        