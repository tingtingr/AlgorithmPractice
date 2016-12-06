class Solution(object):
    def subsetsWithDup(self, nums):
        nums.sort()
        res = []
        self.helper(nums, res, [], 0)
        return res
    def helper(self, nums, res, sub, index):
        res.append(sub)
        for i in range(index, len(nums)):
            if i - 1 > 0 - 1 and nums[i] == nums[i - 1]:
                continue
            self.helper(nums[:i]+nums[1+i:], res, sub + [nums[i]], i)