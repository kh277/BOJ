# 백준 10813

import sys

input = sys.stdin.readline


def solve(N: int, ball: list) -> list:
    DP = [i for i in range(N+1)]

    for start, end in ball:
        DP[start], DP[end] = DP[end], DP[start]

    return DP[1:]


def main():
    N, M = map(int, input().split())

    ball = []
    for _ in range(M):
        ball.append(list(map(int, input().split())))

    print(*solve(N, ball))


main()