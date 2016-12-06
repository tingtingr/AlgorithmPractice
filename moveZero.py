class Solution(object):
    def moveZeroes(self, nums):
        if len(nums) > 1:
            pre = 0
            while pre < len(nums):
                if nums[pre] == 0:
                    cur = pre + 1
                    while cur < len(nums):
                        if nums[cur] != 0:
                            nums[cur], nums[pre] = nums[pre], nums[cur]
                            print(nums)
                            pre += 1
                        cur +=1
                        print(pre, cur)
                pre += 1
        print(nums)        
            

nums = [0,0,1]
nums = [2,1]
nums = [4,2,4,0,0,3,0,5,1,0]
print(nums)
Solution().moveZeroes(nums)