class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for matrix_list in matrix:
            if target in matrix_list:
                return True
        return False
        