class Solution(object):
    def reverse(self, x):
        neg = False
        if x < 0:
            x = -x
            neg =True
        res = 0
        while x > 0 :
            digit = x % 10
            res = res * 10 + digit
            if res > 2**31 -1:
                return 0
            x /= 10
        if neg:
            return -res
        else:
            return res
x = Solution().reverse(1563847412)
print(x)