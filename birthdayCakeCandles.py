#!/bin/python3
import os


# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    newar = sorted(ar, reverse=True)
    count = 0
    for index, value in enumerate(newar):
        if value == newar[0]:
            count += 1
        else:
            break
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
