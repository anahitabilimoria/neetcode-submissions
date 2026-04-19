class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occ = {}
        for i in nums:
            count = nums.count(i)
            if i not in occ.keys():
                occ[i] = count
        sorted_occ = {k: v for k, v in sorted(occ.items(), key=lambda item: item[1], reverse = True)} 
        most_freq = list(sorted_occ.keys())[:k]           
        return most_freq
        