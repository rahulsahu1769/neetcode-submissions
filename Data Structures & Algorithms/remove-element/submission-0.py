class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        counter = 0
        for x in nums:
            if x==val:
                counter+=1
        while counter!=0:
            nums.remove(val)
            counter-=1
        
        return len(nums)
        