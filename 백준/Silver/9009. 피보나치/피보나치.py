# 백준 9009

import sys

input = sys.stdin.readline


def solve(N):
    DP = [0, 1]
    while True:
        nextValue = DP[-1] + DP[-2]
        if nextValue > N:
            break
        else:
            DP.append(nextValue)

    result = []
    index = len(DP)-1
    while True:
        if N == 0:
            break
        if N >= DP[index]:
            result.append(DP[index])
            N -= DP[index]
        index -= 1

    return result[::-1]


# main 함수 ----------
T = int(input())
for i in range(1, T+1):
    N = int(input())
    print(*solve(N))
    