def contains_duplicates (nums):
    if len(nums) == 0:
        return False

    seen_numbers = set(nums)
    if len(seen_numbers) == len(nums):
        return False
    else:
        return True

print (contains_duplicates([1,2,3,1]))
print (contains_duplicates([1,2,3,4]))
print (contains_duplicates([1,1,1,3,3,4,3,2,4,2]))
print (contains_duplicates([]))