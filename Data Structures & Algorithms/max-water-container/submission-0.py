class Solution:
    def maxArea(self, height):
        left = 0 
        right = len(height) - 1
        best_area = 0

        while left < right: 
            width = right - left
            area = width * min(height[left], height[right])
            best_area = max(best_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return best_area