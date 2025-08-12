from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    arr_len = len(nums)
    l_multi = 1
    r_multi = 1
    l_arr = [1] * arr_len
    r_arr = [1] * arr_len
            
    for i in range (arr_len):
        j = -i -1
        l_arr[i] = l_multi
        r_arr[j] = r_multi
        l_multi *= nums[i]
        r_multi *= nums[j]
                
    return [l_arr * r_arr for l_arr, r_arr in zip(l_arr, r_arr)]

print (productExceptSelf([1,2,3,4]))
print (productExceptSelf([-1,1,0,-3,3]))
