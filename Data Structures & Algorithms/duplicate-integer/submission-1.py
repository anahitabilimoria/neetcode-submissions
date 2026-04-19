class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in nums:
            count = nums.count(i)
            if count > 1:
                return True
        return False