from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        queue = [] # like PriorityQueue, remain the top k value
        result = []
        for i in range(len(nums)):
            # judge whether the first item is in window
            if queue and queue[0] < i - k + 1:
                print("queue[0] is {0}, i is {1},k is 3, i - k +1 is {2}".format(queue[0], i, i - k + 1))
                print("pop queue")
                queue.pop(0)
                print(queue)
            # update the queue 
            while queue and nums[queue[-1]] < nums[i]:
                print("queue and nums[queue[-1]] < nums[i]")
                queue.pop()
            queue.append(i)

            #after i > k - 1, output the max value
            if queue and i >= k - 1:
                result.append(nums[queue[0]])
        return result
    
arr = [1,2,3,4,5,6,7,8,9]
k = 3
Solution().maxSlidingWindow(arr,k)