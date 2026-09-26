class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic = defaultdict(int)
        ans = []
        lim = len(nums)/3
        for x in nums:
            dic[x] += 1
        
        for k, v in dic.items():
            if v > lim:
                ans.append(k)

        return ans