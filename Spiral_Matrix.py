from typing import List

def spiralOrder(matrix: List[List[int]]) -> List[int]:
    result = []
    if not matrix or not matrix[0]:
        return result
    left, right = 0, len(matrix[0]) - 1
    top, bottom = 0, len(matrix) - 1
    while left <= right and top <= bottom:
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
    return result

print (spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))  # Example usage
print(spiralOrder([[2,5],[8,4],[0,-1]]))  # this one fails