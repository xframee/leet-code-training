from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:

    result = []
    my_c = {}

    for num in nums:
        if num in my_c:
            my_c[num] += 1
        else:
            my_c[num] = 1

    sorted_numbers_by_frequence = sorted(my_c.items(), key=lambda x:x[1], reverse=True)

    for i in range (k):
        result.append(sorted_numbers_by_frequence[i][0])

    return result


print (topKFrequent([1,1,1,2,2,3], 2))
print (topKFrequent([1], 1))
print (topKFrequent([1,1,1,2,2,3], 2))

