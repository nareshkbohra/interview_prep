from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.sum_matrix = self.build_sum_matrix(matrix)

    def build_sum_matrix(self, matrix):
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        sum_matrix = [[0] * num_cols for _ in range(num_rows)]
        sum_matrix[0][0] = matrix[0][0]

        for i in range(1, num_cols):
            sum_matrix[0][i] = sum_matrix[0][i - 1] + matrix[0][i]
        for i in range(1, num_rows):
            sum_matrix[i][0] = sum_matrix[i - 1][0] + matrix[i][0]
        for i in range(1, num_rows):
            for j in range(1, num_cols):
                sum_matrix[i][j] = matrix[i][j] + sum_matrix[i - 1][j] + sum_matrix[i][j - 1] - sum_matrix[i - 1][j - 1]
        return sum_matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        leftRemoved = False
        topRemoved = False
        result = self.sum_matrix[row2][col2]
        if col1 > 0:
            leftRemoved = True
            result -= self.sum_matrix[row2][col1 - 1]
        if row1 > 0:
            topRemoved = True
            result -= self.sum_matrix[row1 - 1][col2]
        if leftRemoved and topRemoved:
            result += self.sum_matrix[row1 - 1][col1 - 1]
        return result


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
board = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
for row in board:
    print("\t".join(str(i) for i in row))
print("-------------")
mat = NumMatrix(board)
queries = [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]
for query in queries:
    res = mat.sumRegion(*query)
    print(res)
