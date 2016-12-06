def equalsum(nums):
	if not nums:
		return -1
	if len(nums) == 1:
		return 0
	sumV = sum(nums)
	left = 0
	right = sumV - nums[0]
	for i in range(1,len(nums)):
		print(left, right)
		right -= nums[i]
		left += nums[i - 1] 
		if left == right:
			return i
	return -1

nums = [1,2,3,2,1]
print(equalsum(nums))
time complexity is o(n)
space complexity is o(1)
# so when i = 0
# left = 0-
# right = sumV - nums[i]

# when i = 1
# left = left + nums[ i - 1]
# right = right - nums[i]