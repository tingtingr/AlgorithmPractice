import heapq,sys
class Solution(object):
    def mergeKLists(self, lists):
        heap = []
        res = []
        for (index, arr) in enumerate(lists):
                if len(arr) == 0:
                    continue
                heapq.heappush(heap, (arr[0],index, 0))
        
        while len(heap) != 0:
            root = heap[0]
            val = root[0]
            index = root[1]
            position = root[2]
            
            heapq.heappop(heap)
            res.append(val)
            if position + 1 < len(lists[index]):
                heapq.heappush(heap,(lists[index][position + 1], index, position + 1))
        return res

lists = [[1,2,3,4],[1,5,9,22],[-1,4,9,102]]
arr = [2,3,1,4,5,6,8,7,10,9]
arr2 = arr * 2
#print(arr)
#print(enumerate(arr))
print(Solution().mergeKLists(lists))