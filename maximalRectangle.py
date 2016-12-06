class Solution(object):
    def maximalRectangle(self, matrix):
        row = len(matrix)
        if row == 0:
            return 0
        col = len(matrix[0])
        dp = [[0 for i in range(col)] for j in range(row + 1)]
        maxArea = 0
        print(dp)
        for i in range(row):
            for j in range(col):
                print(i, j)
                if matrix[i][j]  ==  1:
                    dp[i + 1][j] = dp[i][j] + 1
                else:
                    dp[i + 1][j] == 0
        print(dp)
        for i in range(row):
            print(dp[i + 1])
            curArea = self.helper(dp[i + 1])
            print(curArea, maxArea)
            maxArea = max(maxArea, curArea)
            
        return maxArea
        
    def helper(self, arr):
        stack = []
        arr.append(-1)
        maxArea = 0
        i = 0 
        print(arr)
        while i < len(arr):
            print(stack)
            if len(stack) == 0 or arr[stack[0]] < arr[i]:
                stack.insert(0, i)
                i += 1
            else:
                curArea = 0
                top = stack[0]
                del stack[0]
                if len(stack) == 0:
                    curArea = arr[top] * i
                else:
                    curArea = arr[top] * (i - stack[0] - 1)
                maxArea = max(maxArea, curArea)
        return maxArea

matrix =[[1]]
print(Solution().helper([1]))
print(Solution().maximalRectangle(matrix))