class Solution(object):
    def removeDuplicates(self, nums):
        res = 0
        if nums:
            i = 0
            while i+1 < len(nums):
                print(i,i+1)
                while nums[i] == nums[i + 1] and i+1 < len(nums):
                    del nums[i]
                    i += 1
                i += 1
        print(nums)
        return len(nums)
nums= [1,1,1]
Solution().removeDuplicates(nums)