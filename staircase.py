#!/bin/python3


# Complete the staircase function below.
def staircase(n):
    x = 1
    while x <= n:
        print(' ' * (n - x) + '#' * x)
        x += 1


if __name__ == '__main__':
    n = int(input())

    staircase(n)

