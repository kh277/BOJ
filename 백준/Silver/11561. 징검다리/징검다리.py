# 백준 11561

import io
import math

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N):
    return (math.isqrt(1+8*N) - 1)//2


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(solve(N))


main()
