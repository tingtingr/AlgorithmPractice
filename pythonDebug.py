import math
class Solution(object):
  def search(self, nums, target):
          return self.searchInRotate(nums, 0, len(nums) - 1, target)
          
  def searchInRotate(self, nums, start, end, target):
      if target == nums[start]:
          return start
      if target == nums[end]:
          return end
      mid = (end - start) / 2 + start
      if target == nums[mid]:
          return mid
      while start + 1 < end:
          mid = (end - start) / 2 + start
          print("start is " + str(nums[start]))
          print("mid is " + str(nums[mid]))
          print("end is " + str(nums[end]))
          if nums[mid] <= nums[start]:
              print("mid < start")
              print("start is " + str(nums[start]))
              print("mid is " + str(nums[mid]))
              print("end is " + str(nums[end]))
              if target > nums[start]:
                  print("target > start")
                  print("start is " + str(nums[start]))
                  print("mid is " + str(nums[mid]))
                  print("end is " + str(nums[end]))
                  return self.binsearch(nums, start, mid, target)
              if target <= nums[start]:
                  print("target < start")
                  print("start is " + str(nums[start]))
                  print("mid is " + str(nums[mid]))
                  print("end is " + str(nums[end]))
                  return self.searchInRotate(nums, mid, end, target)
          if nums[mid] > nums[end]:
              print("mid > end")
              print("start is " + str(nums[start]))
              print("mid is " + str(nums[mid]))
              print("end is " + str(nums[end]))
              if target < nums[end]:
                  print("target < end")
                  print("start is " + str(nums[start]))
                  print("mid is " + str(nums[mid]))
                  print("end is " + str(nums[end]))
                  return self.searchInRotate(nums, mid, end, target)
              if target >= nums[end]:
                  print("target > end")
                  print("start is " + str(nums[start]))
                  print("mid is " + str(nums[mid]))
                  print("end is " + str(nums[end]))
                  return self.binsearch(nums, start, mid, target)
          return self.binsearch(nums, start, end, target)      
      return self.binsearch(nums, start, end, target)
  def binsearch(self, nums, start, end, target):
      while start + 1 < end:
          mid = (end - start) /2 + start
          if target >= nums[mid]:
              start = mid
          else:
              end = mid     
      if nums[start] == target:
              return start
      if nums[end] == target:
              return end
      return -1
      
def myAtoi(self, str):
        res = 0
        neg = False
        signCount = 0
        for i in range(len(str)):
            c =  str[i]
            temp = ord(c) - 48
            if temp >= 0 and temp <= 9:
                res = res * 10 + temp
            else:
                signCount += 1
                print(signCount)
                
        if signCount > 1:
            return 0
        elif len(str) > 0 and str[0] == '-':
            return res * (-1)
        else:
            return res
          
arr = [4,5,6,7,8,1,2,3]
target = 8
print ("arr is " + str(arr))
print ("target is " + str(target))
print(Solution().myAtoi("123"))