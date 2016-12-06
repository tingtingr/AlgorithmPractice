#Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

#Range Sum Query 2D
#The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

#Example:
#Given matrix = [
#  [3, 0, 1, 4, 2],
#  [5, 6, 3, 2, 1],
#  [1, 2, 0, 1, 5],
#  [4, 1, 0, 1, 7],
#  [1, 0, 3, 0, 5]
#]

#sumRegion(2, 1, 4, 3) -> 8
#sumRegion(1, 1, 2, 2) -> 11
#sumRegion(1, 2, 2, 4) -> 12

class NumMatrix(object):
    def __init__(self, matrix):
        self.matrix = matrix
        self.dp = self.getDP(matrix)

    def sumRegion(self, row1, col1, row2, col2):
        self.printMatrix(self.dp)
        print((row1,col2 + 1),(row2 + 1,col1),(row1,col1))
#        print(self.dp[row1 - 1][col2 - 1], self.dp[row2 - 1][col1 - 1], self.dp[row1 - 1][col1 - 1])
        remain = self.dp[row1][col2 + 1] + self.dp[row2 + 1][col1] - self.dp[row1][col1]
        print(remain)
        return self.dp[row2 + 1][col2 + 1] - remain
        
    def getDP(self, matrix):
        col = len(self.matrix[0])
        row = len(self.matrix)
        dp = [[ 0 for i in range(col + 1)] for j in range(row + 1)]
        for i in range( 1, row + 1):
            for j in range(1, col + 1):
                matrix[i - 1][j - 1]
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + matrix[i - 1][j - 1]
        return dp
    def printMatrix(self, matrix):
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            for j in range(col):
                print(matrix[i][j]),
            print("\b")
matrix = [[3, 0, 1, 4, 2],[5, 6, 3, 2, 1],[1, 2, 0, 1, 5],[4, 1, 0, 1, 7],[1, 0, 3, 0, 5]]
NumMatrix(matrix).printMatrix(matrix)
print(NumMatrix(matrix).sumRegion(2, 1, 4, 3))
#print(NumMatrix(matrix).sumRegion(1, 1, 2, 2))
#print(NumMatrix(matrix).sumRegion(1, 2, 2, 4))