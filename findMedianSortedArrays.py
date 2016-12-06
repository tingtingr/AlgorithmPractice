class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        print(nums1,nums2)
        if bool(nums1) ^ bool(nums2):
            x= []
            if not nums1 :
                x = nums2
            else:
                x = nums1
            return self.getMedian(x)
        if len(nums1) + len(nums2) < 5:
            x = sorted(nums1 + nums2)
            y = self.getMedian(x)
            # print("final return")
            # print(y)
            return y
        else:
            m1 = self.getMedian(nums1)
            m2 = self.getMedian(nums2)
            if m1 == m2:
                return m1
            else:
                l1 = self.binsearch(nums1,m1)
                l2 = self.binsearch(nums2,m2)
                if m1 < m2:

                    self.findMedianSortedArrays(tuple1[1], tuple2[0])
                else:
                    print("m1 > m2")
                    self.findMedianSortedArrays(tuple1[0],tuple2[1])
                    
    def getMedian(self, nums):
        mid = len(nums) / 2
        if len(nums) % 2 == 0:
            res = (nums[mid - 1] + nums[mid]) * 1.0/ 2
        else:
            res = nums[mid]
        return res

    def binsearch(self,nums, target):
        start = 0
        end = len(nums) - 1
        left = []
        right = []
        while start + 1 < end:
            mid = (end - start ) / 2 + start
            if nums[mid] == target:
                return [mid]
            if nums[mid] > target:
                end = mid
            else:
                start = mid
        return [start,end]
# [2,4,6,8]
# return the previous the index or the prvious one
# target is 5
# classically to return the next index so where to insert not this time
# [2,4,6,8]
# mid = 4 /2 = 2
# nums[mid] = 6
# 6 > target
# end = 2
# search [2,4,6]
# start = 0, end = 2
# mid = 1
# nums[mid] = 4
# nums[mid] < target
# start = mid 
# round 3
# start = 1 end = 2
# break
# true median : 7
nums1 = [1,2,5,8,10,11,19,20]
nums2 = [2,4,6,7,9]
nums1 = [1,5]
nums2 = [1,2,3]


https://discuss.leetcode.com/topic/16797/very-concise-o-log-min-m-n-iterative-solution-with-detailed-explanation/2




double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
    int N1 = nums1.size();
    int N2 = nums2.size();
    if (N1 < N2) return findMedianSortedArrays(nums2, nums1);   // Make sure A2 is the shorter one.
    
    if (N2 == 0) return ((double)nums1[(N1-1)/2] + (double)nums1[N1/2])/2;  // If A2 is empty
    
    int lo = 0, hi = N2 * 2;
    while (lo <= hi) {
        int mid2 = (lo + hi) / 2;   // Try Cut 2 
        int mid1 = N1 + N2 - mid2;  // Calculate Cut 1 accordingly
        
        double L1 = (mid1 == 0) ? INT_MIN : nums1[(mid1-1)/2];  // Get L1, R1, L2, R2 respectively
        double L2 = (mid2 == 0) ? INT_MIN : nums2[(mid2-1)/2];
        double R1 = (mid1 == N1 * 2) ? INT_MAX : nums1[(mid1)/2];
        double R2 = (mid2 == N2 * 2) ? INT_MAX : nums2[(mid2)/2];
        
        if (L1 > R2) lo = mid2 + 1;     // A1's lower half is too big; need to move C1 left (C2 right)
        else if (L2 > R1) hi = mid2 - 1;    // A2's lower half too big; need to move C2 left.
        else return (max(L1,L2) + min(R1, R2)) / 2; // Otherwise, that's the right cut.
    }
    return -1;
} 

    def findMedianSortedArrays(self,nums1,nums2):
        N1 = len(nums1)
        N2 = len(nums2)
        if N1 < N2:
            return self.findMedianSortedArrays(num2,nums1)
        if N2 == 0:
            return (nums1[N1 - 1 / 2] *1.0 +num1[N1/2]) / 2
        lo = 0
        hi = N2 * 2
        while lo + 1 < hi:
            mid2 = (hi - lo) / 2 + lo
            mid1 = N1 + N2 - mid2

            L1 




x = Solution().findMedianSortedArrays(nums1,nums2)
print(x)