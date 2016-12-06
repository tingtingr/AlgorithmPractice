import sys
class Solution(object):
#    def minimumTotal(self, tri):
#        res = [[sys.maxsize for j in range(len(tri[-1]) + 2)] for i in range(len(tri))]
#        self.printArr(res)
#        res[0][1] = tri[0][0] 
#        for i in range(1,len(tri)):
#            for j in range(len(tri[i])):
#                print(i,j)
#                print(tri[i][j],min(min(res[i - 1][j], res[i - 1][j +1]), res[i - 1][j + 2]))

#                res[i][j + 1] = tri[i][j] + min(res[i - 1][j +1], res[i - 1][j + 2])
#        self.printArr(res)
#        return min(res[-1])
#    bottom up solution
    def minimumTotal(self, tri):
        res = tri[-1]
        for i in range(len(tri) -  2, -1, -1):
            for j in range(len(tri[i])):
                res[j] = tri[i][j] + min(res[j + 1], res[j])
        return res[0]
        
        
    def printArr(self, arr):
        col = len(arr[0])
        row = len(arr)
        for i in range(row):
            for j in range(col):
                print(arr[i][j]),
            print("\n")
arr=[[2],[3,4],[6,5,7],[4,1,8,3]]
arr1 = [[-1],[3,2],[-3,1,-1]]
print(Solution().minimumTotal(arr1))