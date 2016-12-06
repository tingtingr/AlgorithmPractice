class Solution(object):
    def isPerfectSquare(self, num):
        start = 1
        end = num / 2
        while start + 1 < end:
            print(start,end)
            mid = (end - start) / 2 + start
            if mid**2 > num:
                end = mid
            else:
                start = mid
        print(start,end)
        if start**2 == num or end**2 == num:
            return True
        else:
            return False
num = 14
print(Solution().isPerfectSquare(num))