class Solution(object):
    def quickSort(self, arr):
        return self.quick(arr, 0, len(arr) - 1)
        
    def quick(self, arr, lo, hi):
        if lo < hi:
            p = self.partition(arr, lo, hi)
            self.quick(arr, lo, p - 1)
            self.quick(arr, (p + 1), hi)
        else:
            return
    def partition(self, arr, low, high):
        pivot = arr[high]
        wall = low
        for i in range(low, high):
            if arr[i] <= pivot:
                self.swap(arr, wall, i)
                wall += 1
        self.swap(arr, wall, high)
        return wall
        
    def swap(self,arr,i,j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        
arr = [9,8,7,6,5,4,3,2,1]   
# Solution().quickSort(arr)

def quickSort2(nums):
    def quick(lo,high,nums):
        if lo < high:
            p = partition(lo,high,nums)
            quick(lo,p,nums)
            quick(p+1,high,nums)
    def partition(low, high, nums):
        pivot = high
        wall = low
        for i in range(low,high):
            if nums[i] <= pivot:
                nums[i],nums[wall]= nums[wall],nums[i]
                wall += 1
        nums[pivot],nums[wall] = nums[wall],nums[pivot]
        return wall

    return quick(0,len(nums) - 1, nums)

    
print(arr)
quickSort2(arr)
print(arr)