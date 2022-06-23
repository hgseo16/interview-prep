array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]

############################################################

# Approach: 1
# Using iteration
# Time O(n) | Space O(1)

def isValidSubsequence(array, sequence):

    index = 0
    size = len(sequence)

    for i in array:

        if i == sequence[index]:
            index += 1

        if index == size:
            return True

    return False


print(isValidSubsequence(array, sequence))