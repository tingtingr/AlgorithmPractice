kth smallest element, starting from 1
def quickselect(nums, k):
	def partition(nums):
		pivot = len(nums) - 1
		l = 0
		r = len(nums) - 1
		while l < r:
			if nums[l] <= nums[pivot]:
				l += 1
			if nums[r] > nums[pivot]:
				r -= 1
			nums[l],nums[r] = nums[r],nums[l]
		return 
	p = partition(nums)
