class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        d = {}
        for i in range(len(nums)):
            if target-nums[i] in d:
                ans.append(d.get(target-nums[i]))
                ans.append(i)
            d[nums[i]]=i
        
        return ans
        