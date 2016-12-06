class Solution(object):
    def MaxHeight(self, cuboid):
        max_height = 0
        for row in range(len(cuboid)):
            for col in range(len(cuboid[row])):
                if cuboid[row][col] > max_height:
                    max_height = cuboid[row][col]
        return max_height

    def largest3D(self,cuboid):
        max_cub = 0
        max_height = self.MaxHeight(cuboid)
        for height in range(max_height):
            plane = []
            for row in range(len(cuboid)):
                row_value = []
                for col in range(len(cuboid[row])):
                    if cuboid[row][col] > height:
                        row_value.append(0)
                    else:
                        row_value.append(1)
                plane.append(row_value)
            cub  = (height + 1) * self.largest2D(plane)
            if cub > max_cub:
                max_cub = cub
            return max_cub

    def largest2D(self, plane):
        max_rect = 0
        for row in range(len(plane)):
            histogram = []
            for col in range(len(plane[row])):
                if plane[row][col] == 0:
                    height += 1
                else:
                    break
                histogram.append(height)
            area = self.largestArea(histogram)
            max_rect = max(max_rect,area)
            return max_rect
    def largestArea(self, histogram):
        stack = []
        index = 0
        histogram.append(-1)
        max_area = 0
        while index < len(histogram):
            if len(stack) == 0 or histogram[stack[0]] <= histogram[index]:
                stack.insert(0, index)
                index += 1
            else:
                cur_area = 0
                top = stack[0]
                del stack[0]
                if len(stack) == 0:
                    cur_area = histogram[top] * index
                else:
                    cur_area = histogram[top] * (index - 1 - stack[0])
                max_area = max(max_area, cur_area)
        return max_area