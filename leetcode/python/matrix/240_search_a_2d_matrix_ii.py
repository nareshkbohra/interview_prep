from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        currRow = 0
        currCol = cols - 1
        while currRow < rows and currCol >= 0:
            currValue = matrix[currRow][currCol]
            if currValue == target:
                return True
            if currValue > target:
                currCol -= 1
            else:
                currRow += 1

        return False
