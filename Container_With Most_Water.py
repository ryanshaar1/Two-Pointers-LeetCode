class Solution(object):
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        best_sum = 0

        while left < right:
            if height[left] < height[right]:
                best_sum = best_sum if best_sum > height[left] * (right - left) else height[left] * (right - left)
                left += 1
            else:
                best_sum = best_sum if best_sum > height[right] * (right - left) else height[right] * (right - left)
                right -= 1

        return best_sum

