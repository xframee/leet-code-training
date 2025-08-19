from typing import List

def maxArea(height: List[int]) -> int:
    max_area = 0

    for i in range (len(height)):
        for j in range (i+1, len(height)):
            area = min(height[i], height[j]) * (j-i)
            if area > max_area:
                max_area = area

    return max_area

def maxArea2(height: List[int]) -> int:
    best = 0
    
    l, r = 0, len(height) - 1
    
    while l < r:
        area = min(height[l], height[r]) * (r - l)
        if area > best:
            best = area
        
        if height[l] <= height[r]:
            l +=1
        else:
            r -= 1
    
    return best

print (maxArea2([1,8,6,2,5,4,8,3,7]))
print (maxArea2([1,1]))