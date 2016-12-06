import heapq
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        res = []
        if len(nums) == 0:
            return res
        if 0 < len(nums) <= k:
            return [max(nums)]
        heap = []
        for i in range(k):
            heapq.heappush(heap,(-nums[i],i))
        maxV = - heap[0][0]
        maxIndex = heap[0][1]
        res.append(nums[maxIndex])
        for i in range(k, len(nums)):
            while 0 < maxIndex < i - k:
                heapq.heappop(heap)
                maxIndex = heap[0][1]
            if maxIndex == i - k:
                print("equal")
                heapq.heappop(heap)
#                heapq.heappush(heap, (-nums[i],i))
                
                print("MaxIndex"),
                print(maxIndex)
            else:
                print("not equal")
                if nums[i] > nums[maxIndex]:
                    maxIndex = i 
#                heapq.heappush(heap, (-nums[i],i))
                print(heap)
                print(res)
            heapq.heappush(heap, (-nums[i],i))
            maxIndex = heap[0][1]
            res.append(nums[maxIndex])
        return res
#    def maxSlidingWindow(self, nums, k):
#        heap = []
#        res = []
#        push in the negative value, so the minheap becomes the max heap
#        for i in range(k):
#            heapq.heappush(heap,(-nums[i],i))
#        print(heap)
#        maxV = - heap[0][0]
#        maxIndex = heap[0][1]
#        res.append(nums[maxIndex])
#        print("MaxIndex"),
#        print(maxIndex)
#        for i in range(k, len(nums)):
#            print("i : "),
#            print(i)
#        if the one deleted is the maxmium value:
#            while maxIndex <= i - k:
#                    print("hey, maxindex {0} is out side the considered range".format(maxIndex))
#                    print(heap)
#                    print(res)
#                    heapq.heappop(heap)
#                    maxIndex = heap[0][1]
#            if maxIndex == i - k:
#                print("equal")
#                heapq.heappop(heap)
#                heapq.heappush(heap, (-nums[i],i))
#                maxIndex = heap[0][1]
                
#                maxIndex = heap[0][1]
#                print("MaxIndex"),
#                print(maxIndex)
#            else:
#                print("not equal")
#                if nums[i] > nums[maxIndex]:
#                    maxIndex = i 
#                heapq.heappush(heap, (-nums[i],i))
#                print(heap)
#                print(res)
#            res.append(nums[maxIndex])
#        return res
                
    def minHeap(self, nums):
        heap = []
        res = []
        for num in nums:
            heapq.heappush(heap,num)
        for num in nums:
            res.append(heap[0])
            heapq.heappop(heap)
        print(res)
        return res
            
    def maxHeap(self, nums):
        heap = []
        res = []
        neg = [i*-1 for i in nums]
        print(neg)
        for num in neg:
            heapq.heappush(heap, num)
        for num in neg:
            res.append(heap[0] * -1)
            heapq.heappop(heap)
        print(res)
        return res
arr = [9,10,9,-7,-4,-8,2,-6]
k = 5
print(Solution().maxSlidingWindow(arr,k))