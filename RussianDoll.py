class Solution(object):
    def maxEnvelopes(self, env):
        dolls = sorted(env)
        dp = [1 for i in range(len(dolls))]
        maxV = 0
        for i in range(1,len(dolls)):
            cur = i
            if dolls[cur][0] > dolls[maxV][0] and dolls[cur][1] > dolls[maxV][1]:
                dp[i] = dp[i - 1] + 1
                maxV = cur
            else:
                dp[i] = dp[i - 1]
        return dp[-1]
        
    def printMatrix(self, nums):
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                print(nums[i][j]),
            print("\b")

arr = [[5,4],[6,4],[6,7],[2,3]]
arr2 = [[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]
Solution().printMatrix(arr2)
b = sorted(arr2)
print("after sorted")
Solution().printMatrix(b)
Solution().maxEnvelopes(arr2)