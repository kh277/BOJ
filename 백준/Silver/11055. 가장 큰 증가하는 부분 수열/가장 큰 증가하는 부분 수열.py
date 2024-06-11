# 백준 11053

import sys

input = sys.stdin.readline


def solve(N: int, A: list) -> int:
    DP = [A[i] for i in range(N)]

    for cur in range(N):
        for i in range(cur):
            if A[i] < A[cur]:
                DP[cur] = max(DP[cur], DP[i]+A[cur])

    result = max(DP)

    return result



def main():
    N = int(input())
    A = list(map(int, input().split()))

    print(solve(N, A))

main()
