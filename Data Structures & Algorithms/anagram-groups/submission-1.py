class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for x in strs:
            key = "".join(sorted(x))
            d[key].append(x)
        
        return list(d.values())
        

