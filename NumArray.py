class NumArray(object):
    def __init__(self, nums):
        self.nums = nums
        self.dp = self.getDP()
    
    def getDP(self):
        dp = [x for x in self.nums]
        for i in range(1,len(dp)):
            dp[i] = self.nums[i] + dp[i - 1]
        return dp
        
    def sumRange(self, start, end):
        print(self.dp)
        print(self.nums)
        print(self.dp[end],self.dp[start],self.nums[start],start)
        return self.dp[end] - self.dp[start] + self.nums[start]

    def printMatrix(self, matrix):
        col = len(matrix[0])
        row = len(matrix)
        for i in range(row):
            for j in range(col):
                print(matrix[i][j]),
            print("\n")

arr = [-2, 0, 3, -5, 2, -1]
print(arr)
print(NumArray(arr).sumRange(2,5))