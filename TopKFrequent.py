import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        dict = {}
        topKheap = []
        res = []
        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1
        print(dict)
        for (ke, va) in dict.iteritems():
            if len(topKheap) == k:
                if va > topKheap[0][0]:
                    heapq.heapreplace(topKheap,(va,ke))
            else:
                heapq.heappush(topKheap, (va,ke))
            print(topKheap)
        for va, ke in iter(topKheap):
#            res.insert(0,ke)
            res.append(ke)
        print(res)
        return res


arr = [1,1,1,2,3,8,9,5,5,5,2,3]
k = 4
 
Solution().topKFrequent(arr, k)