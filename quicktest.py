def rotate(matrix):
    n = len(matrix)

    # --- Step 1: transpose ---
    for r in range(n):
        for c in range(r + 1, n):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

    # --- Step 2: reverse each row ---
    for r in range(n):
        left, right = 0, n - 1
        while left < right:
            matrix[r][left], matrix[r][right] = matrix[r][right], matrix[r][left]
            left  += 1
            right -= 1

    return matrix

print(rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(rotate([1]))
print(rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))
#print(rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))