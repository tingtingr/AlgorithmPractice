class Solution(object):
    def trap(self, height):
        stack = []
        start = 0
        i = 0
        sumV = 0
        while i < len(height):
            print("index is %d" %(i))
            print("stack is %s" % (stack)),
            print("sumV is %d" % sumV),
            print("\n")
            cur = height[i]
            if len(stack) == 0 or cur < height[stack[-1]]:
                stack.append(i)
                i += 1
            else: 
                print("start popping"),
                while cur < height[stack[-1]] and len(Stack) > 0:
                    top = stack.pop()
                    area = heihgt[cur] - heihgt[top] * (i - top)
                    sumV += area
        return sumV
arr = [0,1,0,2,1,0,1,3,2,1,2,1]
print(arr)
print(Solution().trap(arr))