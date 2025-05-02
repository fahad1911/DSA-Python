def TwoSum(nums, target):

    hash_map = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in hash_map:
            return [hash_map[complement], i]
        
        hash_map[num] = i

    return []

print(TwoSum([2, 7, 5, 11], 9)) #o/p : [0, 1]