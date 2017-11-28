#Given a set of distinct integers, nums, return all possible subsets.

class Solution(object):
    def subsets(self, nums):
        res = []
        self.dfs(sorted(nums), res, [], 0)
        return res
    
    def dfs(self, nums, res, path, start):
        res.append(path)
        for i in range(start, len(nums)):
            self.dfs(nums, res, path+[nums[i]], i + 1)
arr = [1,2,3]
Solution().subsets(arr)
