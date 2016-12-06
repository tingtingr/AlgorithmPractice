class Solution(object):
    def combinationSum(self, candidates, target):
        res = []
        # candidates = sorted(candidates)
        self.helper(res,candidates, target, [])
        print(res)
        return res
    def helper(self,res,candidates, target, sub):
    	print(res,candidates,target,sub,)
        if target == 0:
            res.append(sub)
        
        else:
            for i in range(len(candidates)):
                candidates = candidates[:i] + candidates[i + 1:]
                print(i,candidates)
                if len(candidates) == 0 and target != 0:
                    print("candidate is zero")
                # for j in range(len())
            	# if i + 1 < len(nums) and nums[i] == nums[i + 1]:
            	# 	continue
            	# x = candidates[:i] + candidates[i + 1:]
                # if nums[i] <= target:
                # self.helper(res, candidates[:i] + candidates[i + 1:], target - nums[i], sub + [nums[i]])
                else:
                    self.helper(res, candidates, target - candidates[i], sub + [candidates[i]])
            
        
nums = [2,3,6]
target = 11
Solution().combinationSum(nums, target)



