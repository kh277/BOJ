# 백준 13239

'''
N <= 1000이므로, DP를 이용해 값을 계산하자
'''

import sys

input = sys.stdin.readline


def solve(N: int, K: int) -> int:
    DP = [[0 for _ in range(i+1)] for i in range(N+1)]

    for i in range(1, N+1):
        for j in range(i+1):
            if i == j or j == 0:
                DP[i][j] = 1
            else:
                DP[i][j] = (DP[i-1][j-1] + DP[i-1][j]) % 1000000007

            if i == N and j == K:
                return DP[i][j]


# main 함수 ----------
T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    print(solve(N, K))
