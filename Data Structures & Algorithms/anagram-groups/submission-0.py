class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        an_map = defaultdict(list)
        res = []
        for s in strs:
            sorted_s = tuple(sorted(s))
            an_map[sorted_s].append(s)
        for value in an_map.values(): 
            res.append(value)
        return res
            
            
        