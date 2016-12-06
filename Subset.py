#Given a set of distinct integers, nums, return all possible subsets.

class Solution(object):
#    def subsets(self, arr):
#        result =[]
#        self.backtrack(arr, result, [], 0)
#        self.printArr(result)
#        return result
    
#    def backtrack(self, arr, result, subset, index):
#        if index== len(arr):
#            result.append(subset)
#            return
#        else:
            
#            self.backtrack(arr, result, subset + [arr[index]], index + 1)
#            self.backtrack(arr, result, subset, index + 1)
            
    def subsets(self, arr):
        res = []
        self.dfs(arr, res, [], 0)
        self.printArr(res)
        return res
    def dfs(self,arr, res, subset, start):
        if start == len(arr):
            res.append(subset)
            return
        for i in range(start, len(arr)):
            print("subset is ")
            self.printArr(subset)
            print("self.dfs(arr, res, subset+[{0}], {1})".format(arr[i],i+1))
            self.dfs(arr, res, subset+[arr[i]], i + 1)
            
            
#lintcode Solution recursive
#    def subsets(self, nums):
#        self.printArr(nums)
#        results = []
#        self.search(sorted(nums), results,[], 0)
#        self.printArr(results)
#        return results
        
#    def search(self, nums, results,S, index):
#        if index == len(nums):
#            results.append(S)
#            return
#        self.search(nums, results, S + [nums[index]], index + 1)
#        self.search(nums, results, S, index + 1)
    
    def printArr(self, arr):
        print("[ "),
        for i in range(len(arr)):
            print("{0} ".format(arr[i])),
        print("]")
        
#lintcode iterative, see if it is faster
#    def subsets(self, nums):
#        result = []
#        n = len(nums)
#        sorted(nums)
#        for i in range(1<<n):
#            subset = []
#            print(1<<n)
#            for j in range(n):
#                if (i & (1<<j)) != 0:
#                   subset.append(nums[j])
#            result.append(subset)
#        self.printArr(sorted(result))
#        return result

arr = [1,2,3]
Solution().subsets(arr)
