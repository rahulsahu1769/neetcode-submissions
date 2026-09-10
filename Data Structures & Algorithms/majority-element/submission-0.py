class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        n = len(nums)
        for x in nums:
            dic[x] += 1
        
        for k,v in dic.items():
            if v > n/2:
                return k

