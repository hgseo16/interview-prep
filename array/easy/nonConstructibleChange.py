def nonConstructibleChange(coins):
    # Write your code here.
    coins.sort()
    minChange = 0

    for coin in coins:
        if coin > minChange + 1:
            return minChange + 1
        minChange += coin

    return minChange + 1
