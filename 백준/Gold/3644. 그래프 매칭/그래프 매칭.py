# 백준 3644

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, DP, last):
    if last < N:
        for i in range(last+1, N+1):
            DP[i] = DP[i-1] + DP[i-2]

    return DP[N]


def main():
    DP = [-1 for _ in range(10001)]
    DP[3] = 4
    DP[4] = 7
    last = 4
    while True:
        try:
            N = int(input())
            print(solve(N, DP, last))
            last = max(last, N)
        except:
            break


main()
