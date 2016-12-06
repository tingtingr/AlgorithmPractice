import heapq

#use two heaps, for the median, left side is a max heap, right side is a min heap
#if it is even the push it to the correct side and then let the median be the average of the two tops
#if size if add then push it to the correct side and let the median be the top of the side that was pushed
class MedianFinder:
    def __init__(self):
        self.median = None
        self.leftQueue = []
        self.rightQueue = []
        self.count = 0

    def addNum(self, num):
        if num is None:
            return
        self.count += 1
        if self.median is None:
            self.median = num
        else:
            if self.count % 2 == 0:
                print("self.count % 2 == 0")
                if num > self.median:
                    heapq.heappush(self.rightQueue, float(num))
                    self.maxHeapPush(self.leftQueue, float(self.median))
                else:
                    heapq.heappush(self.rightQueue, float(self.median))
                    self.maxHeapPush(self.leftQueue, float(num))
                self.median = (float(self.rightQueue[0]) + float(-self.leftQueue[0])) / 2

            else:
                if num > self.median:
                    heapq.heappush(self.rightQueue,num)
                    self.median = self.rightQueue[0]
                    heapq.heappop(self.rightQueue)
                else:
                    self.maxHeapPush(self.leftQueue,num)
                    self.median = -self.leftQueue[0]
                    self.maxHeapPop(self.leftQueue)

    def maxHeapPush(self, heap, num):
        heapq.heappush(heap, (-num))
    def maxHeapPop(self, heap):
        num = heap[0]
        heapq.heappop(heap)
        return -num
    
    def findMedian(self):
            return self.median
            
mf = MedianFinder()

mf.addNum(-1)
print(mf.findMedian())
mf.addNum(-2)
print(mf.findMedian())
mf.addNum(-3)
print(mf.findMedian())
mf.addNum(-4)
print(mf.findMedian())
mf.addNum(-5)
print(mf.findMedian())