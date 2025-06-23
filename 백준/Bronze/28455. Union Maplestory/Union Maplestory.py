# 백준 28455

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**9


def solve(N, lev):
    lev.sort(reverse=True)

    accLevel = 0
    accStat = 0
    for i in range(min(42, N)):
        accLevel += lev[i]

        for index, s in enumerate([60, 100, 140, 200, 250, 301]):
            if lev[i] < s:
                accStat += index
                break
    
    return accLevel, accStat


def main():
    N = int(input())
    lev = []
    for _ in range(N):
        lev.append(int(input()))
    print(*solve(N, lev))


main()
