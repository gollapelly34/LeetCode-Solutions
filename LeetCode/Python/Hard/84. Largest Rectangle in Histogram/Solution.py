class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]

                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                area = h * width

                if area > max_area:
                    max_area = area

            stack.append(i)

        while stack:
            h = heights[stack.pop()]

            if stack:
                width = len(heights) - stack[-1] - 1
            else:
                width = len(heights)

            area = h * width

            if area > max_area:
                max_area = area

        return max_area