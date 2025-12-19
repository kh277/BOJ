# 백준 32582

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**9


def solve(A, B, C, D, E):
    return min(A+D, B+E, B+C+D, A+C+E)


def main():
    N = int(input())
    maxSheep = INF
    for _ in range(N):
        A, B, C, D, E = map(int, input().split())
        maxSheep = min(maxSheep, solve(A, B, C, D, E))

    print(maxSheep)


main()
