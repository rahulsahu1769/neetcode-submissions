class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        ans = []
        for x in strs:
            key = "".join(sorted(x))
            d[key].append(x)
        
        for k,v in d.items():
            ans.append(d[k])
        
        return ans
        

