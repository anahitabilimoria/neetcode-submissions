import math 

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        new_arr = []
        for i in range(len(nums)):
            wo_i = nums[:i] + nums[i+1:]
            product = math.prod(wo_i)
            new_arr.append(product)

        return new_arr

        