#!/usr/bin/python3
""" """
import sys

def print_stats(total_size, status_code):
    print("File size: {}".format(total_size))
    for key, value in status_code.items():
        if value > 0:
            print("{}: {}".format(key, value))
    


if __name__ == "__main__":

    total_size = 0
    status_code = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
    counter = 0

    try:
        for line in sys.stdin:
            try:
                counter += 1
                parts = line.split()
                total_size += int(parts[8])
                if parts[7] in status_code:     # "in" pour savoir si parts[6] existe dans status_code
                    status_code[parts[7]] += 1  # on accède à la valeur via la clé
                if counter % 10 == 0:
                    print_stats(total_size, status_code)
            except:
                continue
    except KeyboardInterrupt:
        print_stats(total_size,status_code)
