class Solution(object):
    def permuteUnique(self, nums):
        res = []
        nums = sorted(nums)
        self.helper(nums, res, [],0)
        print(res)
        return res
    def helper(self, nums, res, sub,index):
        # print(nums,sub, index)
        if sub :
            res.append(sub)
        for i in range(index,len(nums)):
            print("helper")
            print(nums, res, sub+[nums[i]],i+1)
            self.helper(nums,res,sub+[nums[i]], i + 1)
nums = [1,1,2,2,3]
nums = [1,2,3]
x = Solution().permuteUnique(nums)