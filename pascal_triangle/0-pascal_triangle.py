#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []  # [] = liste vide
    triange = [[1]]  # première rangée

    for i in range(1, n):
        prev = triange[i - 1]  # rangée précédente
        ligne = [1]  # Pour commencer à un
        for j in range(1, len(prev)):
            result = prev[j - 1] + prev[j]
            ligne.append(result)
        ligne.append(1)
        triange.append(ligne)

    return triange
