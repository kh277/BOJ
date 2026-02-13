# 백준 34838

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N):
    S = (N-1)*(N-2) // 2
    if N % 3 == 0:
        return (S+2) // 3
    return S//3


def main():
    N = int(input())
    print(solve(N))


main()
