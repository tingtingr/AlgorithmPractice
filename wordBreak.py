class Solution(object):
    def wordBreak(self, s, wordDict):
        dp = [False for i in range(len(s)+ 1)]
        dp[0] = True
        for i in range(len(s)):
            for j in range(i, len(s)):
                print(i,j)
                print(dp)
                if dp[i] and s[i:j+1] in wordDict:
                    dp[j + 1] = True
                    print(dp[j+1])
        return dp[-1]
        
    def printMatrix(self, m):
        col = len(m[0])
        row = len(m)
        for i in range(row):
            for j in range(col):
                print("%2d" % (m[i][j])),
            print("\b")
        print("\n")

strs = "leetcode"
dic = {"leet",'code'}
Solution().wordBreak(strs,dic)
