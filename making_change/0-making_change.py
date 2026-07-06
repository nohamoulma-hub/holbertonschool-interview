#!/usr/bin/python3
""" """

def makeChange(coins, total):

    if total <= 0:
        return 0
    if not coins:
        return -1
    min_number_coin = [0] + [float('inf')] * total
    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                min_number_coin[amount] = min(
                    min_number_coin[amount],
                    min_number_coin[amount - coin] + 1
                )
    return min_number_coin[total] if min_number_coin[total] != float('inf') else -1
