# https://leetcode.com/problems/container-with-most-water/?envType=problem-list-v2&envId=array&

def maxArea():
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    left = 0
    right = len(height) - 1
    area = 0

    while left < right:

        width = right - left
        curr = width * min(height[left], height[right])

        area = max(area, curr)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return area


print(maxArea())
