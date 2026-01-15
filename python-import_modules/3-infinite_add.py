#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]  # tous les arguments sauf le script lui-même
    total = 0
    for arg in args:
        total += int(arg)
    print(total)
