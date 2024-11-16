# 백준 5132

import sys

input = sys.stdin.readline

def solve(N, food):
    DP = [0 for _ in range(max(3, N))]

    if N >= 1:
        DP[0] = food[0]
    if N >= 2:
        DP[1] = max(food[0], food[1])
    if N >= 3:
        DP[2] = max(food[1], food[0]+food[2])
    if N >= 4:
        if N >= 3:
            for i in range(3, N):
                DP[i] = max(DP[i-2], DP[i-3]) + food[i]

    return max(DP[N-1], DP[N-2])


# main 함수 ----------
T = int(input())
for i in range(1, T+1):
    N = int(input())
    food = list(map(int, input().split()))
    print("Data Set {a}:".format(a=i))
    print(solve(N, food))
    print()