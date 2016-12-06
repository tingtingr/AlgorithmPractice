import sys
class Solution(object):
#    def coinChange(self, coins, amount):
#        dp = [0 for i in range(amount + 1)]
#        print(dp)
#        for i in range(1, amount + 1):
#            mid =  i // 2
#            sumV = sys.maxsize
#            print(i)
#            for j in range(0, mid):
#                print(i-1-j, j + 1)
#                sumV = min(sumV,dp[i - 1 - j] + dp[j + 1])
#                print(dp)
#            dp[i] = sumV
#            if i in coins:
#                dp[i] = 1
#        return dp[-1]
    def coinChange(self, coins, amount):
        dp = [-1 for i in range(amount + 1)]
        # print(dp)
        for i in range(1, amount + 1):
            if i in coins:
                dp[i] = 1
            else:
                minV = sys.maxsize
                for j in coins:
                    remain = i - j
                    if remain > 0:
                        minV = min(minV, dp[remain])
                dp[i] = minV + 1
            # print(dp)
        return dp[-1]

arr = [1, 2, 5]
k = 7
Solution().coinChange(arr, k)
