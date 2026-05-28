#!/usr/bin/python3
""" Module who calculates the fewest number of operations """


def minOperations(n):

    operation = 0
    diviseur = 2

    if n <= 1:
        return 0

    while n > 1:
        if n % diviseur == 0:
            operation += diviseur
            n = n // diviseur
        else:
            diviseur += 1
    return operation
