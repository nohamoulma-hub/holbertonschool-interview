#!/usr/bin/python3
""" Algo N queens problems"""

import sys

ligne = 0
colonne = 0
queens = []


def valid_entry():

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    argument_entry = sys.argv[1]

    try:
        argument_entry = int(argument_entry)

    except ValueError:
        print("N must be a number")
        exit(1)

    if argument_entry < 4:
        print("N must be at least 4")
        exit(1)

    return argument_entry


def chessboard(queens, colonne, ligne):
    for queen in queens:
        if queen[1] == colonne:
            return False
        if abs(queen[0] - ligne) == abs(queen[1] - colonne):
            return False
    return True


def solve(queens, ligne):
    if ligne == N:
        print(queens)
        return
    for colonne in range(N):
        if chessboard(queens, colonne, ligne):
            queens.append([ligne, colonne])
            solve(queens, ligne + 1)
            queens.pop()


if __name__ == "__main__":
    N = valid_entry()
    queens = []
    solve(queens, 0)  # on démarre à la ligne 0
