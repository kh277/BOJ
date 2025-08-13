# 백준 1475

import io
import math

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N):
    count = [0 for _ in range(10)]
    for i in str(N):
        if int(i) == 9:
            count[6] += 1
        else:
            count[int(i)] += 1
    
    result = 0
    for i in range(10):
        if i == 6:
            result = max(result, math.ceil(count[i]/2))
        else:
            result = max(result, count[i])

    return result


def main():
    N = int(input())
    print(solve(N))


main()
