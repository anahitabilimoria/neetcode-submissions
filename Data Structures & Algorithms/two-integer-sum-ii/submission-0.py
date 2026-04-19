class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            difference = target - numbers[i]
            if difference in list(numbers[:i] + numbers[i+1:]):
                diff_id = numbers.index(difference)
                final = [i, diff_id] if i<diff_id else [diff_id, i]
                final = [i+1 for i in final]
                return final 
        