class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            temp = { val : (ind if ind < i else ind + 1) for ind, val in enumerate(nums[:i] + nums[i+1:])}
            for j in temp.keys():
                if nums[i] + j == target:
                    return [i,temp[j]] if i<temp[j] else [temp[j],i]

        