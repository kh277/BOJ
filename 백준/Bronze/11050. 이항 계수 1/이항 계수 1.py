# 백준 11050


import sys

input = sys.stdin.readline


def solve(N: int, K: int) -> int:
    DP = [[0 for _ in range(N+1)] for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(i+1):
            # 파스칼 삼각형에서 값이 1인 이항계수들
            if i == j or j == 0:
                DP[i][j] = 1
            # 점화식
            else:
                DP[i][j] = (DP[i-1][j-1] + DP[i-1][j]) % 10007

            # 탈출조건
            if i == N and j == K:
                return DP[i][j]


def main():
    N, K = map(int, input().split())
    
    print(solve(N, K))


main()