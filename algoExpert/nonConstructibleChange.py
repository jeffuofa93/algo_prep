def nonConstructibleChange(coins):
    coins.sort()
    count = 0
    for coin in coins:
        if coin < count + 1:
            return count + 1
        count += coin
    return count + 1


"""
Explanation

always sort the array if stuck, trick is that as you cannot create a coin that is greater then the toal + 1
"""
