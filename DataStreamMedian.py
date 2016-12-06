
import heapq

#use two heaps, for the median, left side is a max heap, right side is a min heap

class Solution:
    def medianSlidingWindow(self, nums, n):
        res= []
        heap = [(v, k) for (k, v) in enumerate(nums[:n])]
        heapq.heapify(heap)
        median = heap[n//2]
        leftHeap = heap[:n//2]
        temp = []
        for (v,k) in leftHeap:
            heapq.heappush(temp, (-v,k))
        leftHeap = [(-v,k) for (v,k) in temp]
        rightHeap = heap[n//2 + 1:]
#        Test
        print([(v,k) for (k,v) in enumerate(nums)])
        print("Finished init")
        print("heapLeft : {0} ,heapRight : {1}, median : {2}, heap {3}".format(leftHeap,rightHeap,median,leftHeap + [median] + rightHeap))
        print("\n")
        res.append(median[0])
        for i in range(n,len(nums)):
            #Test
            print("pushing in {0}".format((nums[i],i)))
            
            if median[1] <= i - n:
                print("removing previous median {0}".format(median))
                if nums[i] > median[0]:
                    heapq.heappush(rightHeap,(nums[i],i))
                    median = heapq.heappop(rightHeap)
                else:
                    self.maxHeapPush(leftHeap,(nums[i],i))
                    median = heapq.heappop(leftHeap)
                print("finish now median {0}".format(median))
                
            elif nums[i] >= median[0]: 
                print("nums[i] > median[0]")
                heapq.heappush(rightHeap, (nums[i], i))
                print("rightHeap"),
                print(rightHeap)
                leftHeap = self.maxHeapPush(leftHeap, median)
                print("leftHeap"),
                print(leftHeap)
                median = leftHeap[0]
                leftHeap = self.maxHeapPop(leftHeap)
                
                print("rightHeap"),
                print(rightHeap)
                print("heapLeft : {0} ,heapRight : {1}, median : {2}, heap {3}".format(leftHeap,rightHeap,median,leftHeap + [median] + rightHeap))
                print("\n")
            else:
                leftHeap = self.maxHeapPush(leftHeap, (nums[i],i))
                heapq.heappush(rightHeap,(median))
#                median = leftHeap[0]
#                leftHeap = self.maxHeapPop(leftHeap)
                median = rightHeap[0]
                heapq.heappop(rightHeap)
            res.append(median[0])
            print("res : "),
        print(res)
        return res

    def maxHeapPush(self, heap, (v,k)):
        heap.append((v,k))
        return self.maxHeapify(heap)

    def maxHeapify(self, heap):
        temp =[]
        for (v,k) in heap:
            heapq.heappush(temp,(-v,k))
        temp = [(-v,k) for (v,k) in temp]
        return temp

    def maxHeapPop(self, heap):
        top = heap[0]
        return self.maxHeapify(heap[1:])
            
arr = [1,2,7,7,2]
k = 3
Solution().medianSlidingWindow(arr,k)