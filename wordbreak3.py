class Solution(object):
    def wordBreak(self, s, wordDict):
        dp = [False for i in range(len(s) + 1)]
        dp[0] = True
        for i in range(len(s)):
        	for j in range(i,len(s)):
        		if dp[i] and s[i:j+1] in wordDict:
        			dp[j + 1] = True
        return dp[-1]

    def printMatrix(self, m):
    	for i in range(len(m)):
    		for j in range(len(m[0])):
    			print(m[i][j]);
    		print('\b')
Solution.wordBreak()



class Solution(object):
    def rob(self, nums):
        dp = [0 for i in range(len(nums) + 2)]
        for i in range(len(nums)):
            dp[i + 2] = max(dp[i] + nums[i], dp[i + 1])
            # print(dp)
        return dp[-1]