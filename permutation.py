class Solution(object):
	def permutation(self, nums):
		res = []
		self.helper(nums, res, [])
		return res
	def helper(self, nums, res, sub):
		if not nums:
			res.append(sub)
		for i in range(len(nums)):
			self.helper(nums[:i] + nums[i+1:],res,sub+[nums[i]])
