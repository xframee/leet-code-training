from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:

    for i in range (len(nums)):
        for j in range (i+1, len(nums)):
            if nums[i] + nums [j] == target:
                return [i, j]
            
print (twoSum([2,7,11,15], 9))
print (twoSum([3,2,4], 6))
print (twoSum([3,2,3], 6))
print (twoSum([2,5,5,11], 10))

def optimal_two_sum (nums: List[int], target: int) -> List[int]:
        seen = {}  

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                 return [seen[complement], i]

            seen[num] = i

        return []

print (optimal_two_sum([2,7,11,15], 9))
print (optimal_two_sum([3,2,4], 6))
print (optimal_two_sum([3,2,3], 6))
print (optimal_two_sum([2,5,5,11], 10))