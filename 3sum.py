class Solution(object):
	def threeSum(self, nums):
		res = []
		nums = sorted(nums)
		for i in range(len(nums)):
			if i - 1 >= 0 and nums[i - 1] == nums[i]:
				continue
			target = -nums[i]
			x = i + 1
			y = len(nums) - 1
			# print("target"), 
			# print(target)
			while x < y:
				# print(nums[x],nums[y])
				sumV = nums[x] + nums[y]
				# print(sumV)
				if sumV == target:
					res.append([nums[i],nums[x],nums[y]])
					while x+1 < y and nums[x] == nums[x + 1]:
						x += 1
					while y- 1 > x and nums[y - 1] == nums[y]:
						y -= 1
					x += 1
					y -= 1
				elif sumV > target:
					y -= 1
				else:
					x += 1
# 		print(res)
		return res
nums = [-1,0,1,2,-1,-4]

Solution().threeSum(nums)