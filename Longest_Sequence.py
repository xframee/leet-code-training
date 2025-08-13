from typing import List


def longestConsecutive(nums: List[int]) -> int:
    longest_sequence = 0
    myset = set(nums)

    for num in myset:
        if num - 1 not in myset:
            start = num
            streak = 1
            while start + streak in myset:
                streak += 1
            longest_sequence = max(longest_sequence, streak)

    return longest_sequence

print(longestConsecutive([100,4,200,1,3,2]))
print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
print(longestConsecutive([1,0,1,2]))
