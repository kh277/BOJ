# 백준 17451

import io
import math

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, V):
    result = 0
    foreV = V[N-1]
    for i in range(N-2, -1, -1):
        curV = V[i]
        if foreV <= curV:
            foreV = curV
        else:
            foreV = math.ceil(foreV/curV)*curV

    return foreV


def main():
    N = int(input())
    V = list(map(int, input().split()))
    print(solve(N, V))


main()
