# 백준 1912번

# Brute Force로 풀 경우 O(n^2)의 시간복잡도를 가지므로, 1초 시간제한에 걸림.
# DP를 이용하면 O(n)에 해결 가능.

from sys import stdin
from math import inf

input = stdin.readline


def solve(N: int, A: list) -> int:
    DP = [0 for x in range(N)]

    # 현재까지의 최대값 = max(이전까지의 합 + 현재 값, 현재 값)
    # 점화식 : DP[N] = max(DP[N-1] + A[N], A[N])
    maxNum = -inf
    for x in range(N):
        DP[x] = max(DP[x-1] + A[x], A[x])
        if DP[x] > maxNum:
            maxNum = DP[x]

    return maxNum


def main():
    N = int(input())
    A = list(map(int, input().split()))

    print(solve(N, A))


main()
