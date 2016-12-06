class Solution(object):
    def majorityElement(self, nums):
        cnt1 = 0
        n1 = 0
        for a in nums:
            print(a)
            print(n1,cnt1)
            if cnt1 == 0:
                n1 = a
                cnt1 = 1
            elif a == n1:
                cnt1 += 1
            else:
                cnt1 -= 1
                
        print(n1, cnt1)
        return n1


nums = [3,3,4]

Solution().majorityElement(nums)