class Solution(object):
    def maxCoins(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        dic = {}

        def twoBal(dic, i , j, nums):
            if i > j:
                i,j = j,i

            if (i,j) in dic:
                return dic[(i,j)]
            else:
                res = i * j + j
                dic[(i,j)] = res
                return res

        def helper(nums, dic, index):
            print(nums,dic)
            if len(nums) == 1:
                return 1
            if len(nums) == 2:
                return twoBal(dic,0,1,nums)
            maxV = 0
            for i in range(len(nums)):
                left = nums[i - 1] if i - 1 >= 0 else 1
                right = nums[i + 1] if i + 1 < len(nums) else 1
                val = helper(nums, dic, i)
                maxV = max(val, maxV)
            return maxV
        return helper(nums, dic)

nums = [3,1,5,8]
nums = [9,76,64,21,97,60]
print(Solution().maxCoins(nums))