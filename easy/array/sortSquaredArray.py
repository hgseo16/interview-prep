array = [1, 2, 3, 5, 6, 8, 9]

def sortedSquaredArray(array):
    result = []
    for i in array:
        sqr = i * i
        result.append(sqr)
    result.sort() # for negative numbers
    return result

print(sortedSquaredArray(array))
