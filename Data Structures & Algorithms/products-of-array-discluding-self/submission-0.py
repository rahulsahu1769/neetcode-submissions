class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        d = defaultdict(int)
        for i in range(len(nums)):
            d[i] = nums[i]
        
        for i in range(len(nums)):
            temp = 1
            for k,v in d.items():
                if k != i:
                    temp *= v
            res.append(temp)
        
        return res