from heapq import *
# use heap to keep track of the maximum height that's currently active
# the trick is to use t, which is the value to left, right coordinates as a iterator and when the maxium changes
# we first pop the top and record the position t, and the height top. this is our result.
 
# we also keep track of the records when we push
class Skyline(object):
            
    def getSkyline2(self, arr):
        res = []
        maxH = 0
        points = sorted([(x[0],x[2],'s') for x in arr] + [(x[1],x[2],'e') for x in arr])
        heap = [0]
        for p in points:
            print("now p is"),
            print(p)
            if p[2] =='s' and -p[1] ! = heap[0]:
                print("this is the left edge, so we push "),
                print(p[1])
                heappush(heap, -p[1])
                print(heap)
            if p[2] == 'e'and -p[1] ! = heap[0]:
                print("this is the right edge, so we remove "),
                print(p[1])
                heap.remove(-p[1])
                heapify(heap)
                print(heap)
            curMaxH = -heap[0]
            print("now curMaxH is"),
            print(curMaxH)
            if maxH < curMaxH or maxH > curMaxH:
                res.append([p[0],-heap[0]])
                maxH = curMaxH
            print("now res is"),
            print(res)
        print(res)
        return res
        
        
    def matrixPrint(self,arr):
        maxHeight = 0
        maxwidth = 0
        for l in arr:
            width = l[1]
            height = l[2]
            maxHeight = max(maxHeight,height)
            maxwidth = max(maxwidth,width)
        col = maxwidth + 2
        row = maxHeight + 2
        
        grid = [[ 0 for i in range(col)] for j in range(row)]
#        set up ruler
        for i in range(row):
            for j in range(col):
                if j == 0:
                    grid[i][j] = maxHeight - i + 1
                if i == row - 1:
                    grid[i][j] = j

        for p in arr:
            left = p[0]
            right = p[1]
            height = p[2]
            for i in range(height, 0, -1):
                for j in range(left, right + 1):
                    if i == height or j == left or j == right:
                        grid[row - 1 - i][j] = 1
        self.printMatrix(grid)

    def printMatrix(self, matrix):
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    print("  "),
                else:
                    print("%2d" % (matrix[i][j],)),
            print("\b")
            
    def scanPoints(self, arr):
        res = []
        for p in arr:
            left = p[0]
            right = p[1]
            height = p[2]
            res.append([left,height])
            res.append([right,height])
        print(sorted(res))
        


    def getSkyline(self, LRH):
        skyline = []
        i, n = 0, len(LRH)
        liveHR = []
        while i < n or liveHR:
            if not liveHR or i < n and LRH[i][0] <= -liveHR[0][1]:
                x = LRH[i][0]
                while i < n and LRH[i][0] == x:
                    heappush(liveHR, (-LRH[i][2], -LRH[i][1]))
                    i += 1
            else:
                x = -liveHR[0][1]
                while liveHR and -liveHR[0][1] <= x:
                    heappop(liveHR)
            height = len(liveHR) and -liveHR[0][0]
            if not skyline or height != skyline[-1][1]:
                skyline += [x, height],
        print(skyline)
        return skyline
    
arr = [[2,9,10],[5,12,12],[3,7,15],[15,20,10],[19,24,8]]
arr2 = [[0,2,3],[2,5,3]]
Skyline().matrixPrint(arr)
print(arr)
Skyline().scanPoints(arr)
Skyline().getSkyline2(arr2)
Skyline().getSkyline(arr2)