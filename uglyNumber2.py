from heapq import *
class Solution(object):
    def nthUglyNumber(self, n):
        # for any ugly number x, 2x ,3x, 5x are both ugly number.
        # push the future ugly number in queue the get it out
        primes = [2,3,5]
        heap = [1]
        for i in range(n):
            res = heap[0]
            heappush(heap, res*2)
            heappush(heap, res*3)
            heappush(heap, res*5)
            while res == heap[0]:
                heappop(heap)
            print(heap)
        print(res)
n = 12

Solution().nthUglyNumber(n)