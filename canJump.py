class Solution(object):
    def canJump(self, nums):
        mile = 0
        for i in range(len(nums)):
            if i <= mile:
                mile = max(nums[i] + i, mile)
                if mile >= len(nums) - 1:
                    return True
        return False

arr = [0,2,3]
Solution().canJump(arr)