import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        heap = []
        if k < len(nums):
            return None
        # nlogn
        for num in nums:
            heapq.heappush(heap, num)
            print(heap)
        # nlog worst case
#        while len(heap) > len(num) - k - 1:
#            res = heap[0]
#            heapq.heappop(heap)
        print(res)
        return res

arr = [1,3,4,7,2]
k = 3
Solution().findKthLargest(arr,k)