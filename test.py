array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10

def twoNumberSum(array, targetSum):
    # Write your code here.
    result = []
    cmp_length = len(array) - 1

    for idx, val in enumerate(array):
        for i in array[idx+1:]:
            twoSum = val + i
            if twoSum == targetSum:
                result.append(val)
                result.append(i)

    return result


print(twoNumberSum(array, targetSum))

# Space O(n)
# Time O(n)