class Solution(object):
    def search(self, nums, target):
        if nums == sorted(nums):
            return self.binsearch(nums, 0, len(nums) - 1, target)
        return self.search2(nums, 0, len(nums) - 1, target)


    def search2(self,nums, l, r, target):
        if nums[l] < nums[r]:
            print("inorder")
            return self.binsearch(nums, l, r, target)
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        while l + 1< r:
            mid = (r - l) / 2 + l
            print(nums[l:r+1], nums[mid], target)
            if nums[mid] >= nums[r]:
                print("cond 1")
                if nums[l] <= target <= nums[mid]:
                    print("cond 1a")
                    return self.binsearch(nums, l, mid, target)
                else:
                    print("cond 1b")
                    l = mid + 1
            if nums[mid] < nums[r]:
                print("cond 2")
                if nums[mid] <= target <= nums[r]:
                    return self.binsearch(nums, mid, r, target)
                else:
                    r = mid - 1
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        return -1

    def binsearch(self, nums, i, j, target):
        print("binsearch")
        print(nums[i:j+1], target, i, j)
        while i + 1 < j:
            mid = i + (j - i) / 2
            if nums[mid] <= target:
                i = mid
            else:
                j = mid
        if nums[i] == target:
            return i
        if nums[j] == target:
            return j 
        return -1

nums = [4,5,6,7,8,1,2,3]
target = 8

nums = [3,1,1]
target = 3
# mid = 3
# nums[mid] = 7
# nums[mid] < target:
# search[3:8]
# [7,8,1,2,3] nums [3, 8]
# mid = 2
# nums[mid] = 5
# nums[mid] < nums[r]:
# nums[mid] < target:
# search [3,6] = [7,8,1]
# mid = 4
# numd[mid] = 8 > numd[5] = 1
#  target <= mid
#  binsearch (nums, 3, 4,)



# target
# [4, 5, 6, 7, 8, 1, 2, 3], 8, 5, 7

print(Solution().search(nums,target))
# print(Solution().binsearch([3,5,1],0,1,1))
# print(Solution().binsearch([]))