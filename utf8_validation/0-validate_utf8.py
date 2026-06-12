#!/usr/bin/python3
"""
Module determines if a given data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """ Détermine si une liste d'entiers représente
    un encodage UTF-8 valide. """
    n_bytes = 0  # nombre d'octets de continuation attendus

    for num in data:
        byte = num & 0b11111111  # on ne garde que les 8 bits de poids faible

        if n_bytes == 0:
            if byte >> 7 == 0:           # 0xxxxxxx -> 1 octet
                continue

            elif byte >> 5 == 0b110:     # 110xxxxx -> 2 octets
                n_bytes = 1

            elif byte >> 4 == 0b1110:    # 1110xxxx -> 3 octets
                n_bytes = 2

            elif byte >> 3 == 0b11110:   # 11110xxx -> 4 octets
                n_bytes = 3
            else:
                return False             # préfixe invalide
        else:
            if byte >> 6 != 0b10:        # doit commencer par 10
                return False
            n_bytes -= 1

    return n_bytes == 0
