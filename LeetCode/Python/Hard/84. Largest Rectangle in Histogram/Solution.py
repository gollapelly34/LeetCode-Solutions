class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
          l = []
          max_area = 0

          for i in range(len(heights)):
              min_height = heights[i]

              for j in range(i, len(heights)):
                  if heights[j] < min_height:
                      min_height = heights[j]

                  width = j - i + 1
                  area = width * min_height

                  if area > max_area:
                      max_area = area

          return max_area
        