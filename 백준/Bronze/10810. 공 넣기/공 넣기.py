# 백준 10810

import sys

input = sys.stdin.readline


def solve(N: int, ball: list) -> list:
    DP = [0 for _ in range(N+1)]

    for start, end, num in ball:
        for i in range(start, end+1):
            DP[i] = num

    return DP[1:]


def main():
    N, M = map(int, input().split())

    ball = []
    for _ in range(M):
        ball.append(list(map(int, input().split())))

    print(*solve(N, ball))


main()