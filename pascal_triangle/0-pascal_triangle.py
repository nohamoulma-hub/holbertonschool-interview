#!/usr/bin/python3
"""Module that returns a list of lists of integers
representing Pascal's triangle"""


def pascal_triangle(n):
    """Returns Pascal's triangle of n rows as a list of lists"""
    if n <= 0:
        return []  # [] = liste vide
    triangle = [[1]]  # première rangée

    for i in range(1, n):
        prev = triangle[i - 1]  # rangée précédente
        ligne = [1]  # Pour commencer à un
        for j in range(1, len(prev)):
            result = prev[j - 1] + prev[j]
            ligne.append(result)
        ligne.append(1)
        triangle.append(ligne)

    return triangle
