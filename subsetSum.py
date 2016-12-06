class Solution(object):

    def subsetSum(self, nums, target):
        sorted(nums)
        dp = [[0 for i in range(target + 1)] for j in range(len(nums) + 1)]
#        init
        self.printMatrix(dp)
        for i in range(len(nums) + 1):
            dp[i][0] = 1
        self.printMatrix(dp)
        for j in range(len(nums)):
            for i in range(target):
                if nums[j] > i + 1:
                    
                    dp[j + 1][i + 1] = dp[j][i + 1]
                if nums[j] == i + 1:
                    print("equals")
                    dp[j + 1][i + 1] = 1
                else:
                    dp[j + 1][i + 1] = dp[j][i + 1] | dp[j][i + 1 - nums[j]]
                print(j + 1,i + 1, dp[j + 1][i + 1])
                
        for num in nums:
            index = nums.index(num)
            if i in range(target):
                of
                    dp[index + 1][i + 1] = dp[index][i + 1]
                if num == i:
                    dp[]
                    
        self.printMatrix(dp)
        return dp[-1][-1]

    def printMatrix(self, matrix):
        col = len(matrix[0])
        row = len(matrix)
        for i in range(row):
            for j in range(col):
                print("{0}".format(matrix[i][j])),
            print("\n")
            
arr = [2,3,7,8,10]
target = 11
Solution().subsetSum(arr, target)