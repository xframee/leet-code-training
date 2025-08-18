from typing import List

def maxArea(height: List[int]) -> int:
    max_area = 0

    for i in range (len(height)):
        for j in range (i+1, len(height)):
            area = min(height[i], height[j]) * (j-i)
            if area > max_area:
                max_area = area

    return max_area

print (maxArea([1,8,6,2,5,4,8,3,7]))