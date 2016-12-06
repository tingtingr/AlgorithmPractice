import heapq
# use a maxheap on the left
class Solution(object):
	def findMedian(self, arr):
		halfArr = [-arr[i] for i in range(len(arr) // 2 + 1)]
		
		heapq.heapify(halfArr)
		print(halfArr)
		for i in range(len(arr)//2 + 1, len(arr)):
			temp = halfArr[0]
			print(arr[i])
			if -arr[i] >= temp:
				heapq.heapreplace(halfArr, -arr[i])
				print(halfArr)

		if len(halfArr) % 2 == 0:
			largest = halfArr[0]
			heapq.heappop(halfArr)
			secondLar = halfArr[0]
			return -(largest + float(secondLar)) / 2
		else:
			return -halfArr[0]

arr = [5,3,4,1,6,7,2,9,8,10,11,-1,-4,-9]
print(sorted(arr))

print(Solution().findMedian(arr))

