#!/usr/bin/python3
"""
making change module
"""


def makeChange(coins, total):
    """
    returning fewest number of `coins`
    """
    if (total <= 0):
        return 0

    f_coins = [None] * (total + 1)
    f_coins[0] = 0
    for i in range(1, total + 1):
        f_coins[i] = total + 1

    for coin in coins:
        for i in range(coin, total + 1):
            if f_coins[i - coin] + 1 < f_coins[i]:
                f_coins[i] = f_coins[i - coin] + 1

    if f_coins[total] > total:
        return -1
    else:
        return f_coins[total]
