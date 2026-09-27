class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix[0]) - 1
        row = 0
        while left <= right:
            mid = left + ((right - left) // 2)
            if target > matrix[row][right]:
                row += 1
                if row >= len(matrix):
                    return False
            else:
                if target == matrix[row][mid]:
                    return True
                if target < matrix[row][mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return False