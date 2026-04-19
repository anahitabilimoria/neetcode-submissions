class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for string in strs:
            sorted_str = "".join(sorted(string))
            if sorted_str not in res:
                res[sorted_str] = []
            res[sorted_str].append(string)
        
        return list(res.values())