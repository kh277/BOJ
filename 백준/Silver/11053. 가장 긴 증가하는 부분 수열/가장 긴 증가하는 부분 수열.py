# 백준 11053

import sys

input = sys.stdin.readline


def solve(N: int, A: list) -> int:
    DP = [1 for _ in range(N)]

    for i in range(N):
        for j in range(i+1, N):
            if A[j] > A[i]:
                DP[j] = max(DP[j], DP[i]+1)

    result = 0
    for i in range(N):
        if result < DP[i]:
            result = DP[i]

    return result



def main():
    N = int(input())
    A = list(map(int, input().split()))

    print(solve(N, A))

main()
