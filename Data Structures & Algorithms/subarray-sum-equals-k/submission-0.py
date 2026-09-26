class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        count = 0
        curr_sum = 0
        seen[0] = 1
        for n in nums:
            curr_sum += n
            count += seen[curr_sum-k]
            seen[curr_sum] += 1
        
        return count

        
        