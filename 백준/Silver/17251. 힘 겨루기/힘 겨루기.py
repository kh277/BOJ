# 백준 17251

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, stat):
    maxStat = max(stat)
    maxIndex = []
    for i in range(N):
        if stat[i] == maxStat:
            maxIndex.append(i)
    minData = maxIndex[0] + 1
    maxData = maxIndex[-1]
    gap = N - maxData - minData

    if gap > 0:
        return 'R'
    elif gap < 0:
        return 'B'
    else:
        return 'X'


def main():
    N = int(input())
    stat = list(map(int, input().split()))
    print(solve(N, stat))


main()
