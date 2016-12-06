
import sys

class Solution(object):

    def maxProduct(self, nums):
        if len(nums) == 0:
            return 0
        pos = neg = maxV = nums[0]
        self.printArr(nums)
        for i in range(1,len(nums)):
            a = pos * nums[i]
            b = neg * nums[i]
            c = nums[i]
            pos = max(max(a,b),c)
            neg = min(min(a,b),c)
            maxV = max(maxV, pos)
            print("pos : {0} & neg : {1} & max : {2}".format(pos, neg, maxV))
        return maxV

    def printMatrix(self, matrix):
        col = len(matrix[0])
        row = len(matrix)
        for i in range(row):
            for j in range(col):
                print(matrix[i][j]),
            print("\t")
    def printArr(self, arr):
        print("[")
        for i in range(len(arr)):
            print(arr[i]),
        print("]")
            
arr = [2,3,-2,-8,4]
print(Solution().maxProduct(arr))