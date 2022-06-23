array = [3, 5, -4, 4, 8, 11, 1, -1, 6]
targetSum = 10

# Approach: 1
# Using two for loops
#  Time O(n^2) | Space O(1)

# def twoNumberSum(array, targetSum):
#     result = []
#     cmp_length = len(array) - 1
#
#     for idx, val in enumerate(array):
#         for i in array[idx+1:]:
#             twoSum = val + i
#             if twoSum == targetSum:
#                 result.append(val)
#                 result.append(i)
#
#     return result
#
#
# print(twoNumberSum(array, targetSum))

############################################################

# # Approach: 2
# # Using hash table
# # Time O(n) | Space O(n)
#
# def twoNumberSum(array, targetSum):
#     nums = {}
#     for num in array:
#         potentialMatch = targetSum - num
#         if potentialMatch in nums:
#             return [potentialMatch, num]
#         else:
#             nums[num] = True
#     return []
#
# print(twoNumberSum(array, targetSum))

############################################################

# Approach: 3
# Using sorted array
# Time O(n log n) | Space O(1)

def twoNumberSum(array, targetSum):
    array.sort()
    print(array)
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1

print(twoNumberSum(array, targetSum))