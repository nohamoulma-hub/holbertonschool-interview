#!/usr/bin/python3
""" Module Prime Game"""


def isWinner(x, nums):
    """ function who determinate the winner of the game """
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n < 2:
            ben_wins += 1
        else:
            is_prime = [True] * (n + 1)
            is_prime[0] = False
            is_prime[1] = False

            for i in range(2, n + 1):
                if is_prime[i]:

                    for multiple in range(2*i, n + 1, i):
                        is_prime[multiple] = False

            nb_premiers = is_prime.count(True)

            if nb_premiers % 2 == 1:
                maria_wins += 1
            else:
                ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    if ben_wins > maria_wins:
        return "Ben"
    else:
        return None
