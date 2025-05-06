def max_sub_array(nums):
    max_sum = nums[0]
    current_sum = 0

    for num in nums:
        current_sum += num
        max_sum = max(max_sum, current_sum)
        
        if current_sum < 0:
            current_sum = 0

    return max_sum

print(max_sub_array([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6 (subarray: [4,-1,2,1])
print(max_sub_array([1]))  # Output: 1 (subarray: [1])