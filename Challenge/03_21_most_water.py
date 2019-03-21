# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

# Note: You may not slant the container and n is at least 2.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max = 0
        for i in range(len(height)):
            for a in range(i, len(height)):
                # length = abs(i - a)
                # height_2 = min(height[i], height[a])
                container = (abs(i - a)) * (min(height[i], height[a]))
                if max < container:
                    max = container
        return max

