class Solution(object):
    def largestRectangleArea(self, heights):
        stack = [0]
        top = 0
        area = 0
        maxArea = 0
        index = 0
        for i in range(1,len(heights)):
            if heights[i] > heights[stack[0]]:
                stack.insert(0, i)
            else:
                if len(stack) > 0 :
                    print(stack)
                    if heights[stack[0]] > heights[i]:
                        del stack[0]
            print(stack)
#        for i in range(len(stack)):
#            if len(stack) == 0:
#                area = heights[stack[0]] * index
#            else:
#                area = heights[stack[0]] * (index - stack[0] - 1)
#                del stack[0]
#            maxArea = max(area, maxArea)
#        print(maxArea)
#        return maxArea

arr = [2,1,5,6,2,3]
Solution().largestRectangleArea(arr)
                