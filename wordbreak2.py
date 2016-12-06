class Solution(object):
    def wordBreak(self, s, wordDict):
        res = []
        def isbreakable(s, wordDict):
            dp = [True] + [False for x in range(len(s))]
            for i in range(len(s)):
                for j in range(i,len(s)):
                    if dp[i] and s[i:j+1] in wordDict:
                        dp[j+1] = True
            return dp[-1]
        if isbreakable(s, wordDict):
            nums = list(s)
            dp = [True] + [False for i in range(len(s))]
            self.helper(res, nums, wordDict, [])
        return res
    def helper(self, res, nums, wordDict, sub):
        # print(sub, nums)
        if len(nums) == 0:
            res.append(" ".join(sub))
        for i in range(len(nums)):
            if "".join(nums[:i+1]) in wordDict:
                self.helper(res, nums[i+1:], wordDict, sub+["".join(nums[:i+1])])
