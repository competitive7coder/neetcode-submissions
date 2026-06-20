class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        area = 0

        while left < right:
            h = min(heights[left], heights[right])
            w = right - left
            curr_area = h * w
            area = max(area, curr_area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return area

