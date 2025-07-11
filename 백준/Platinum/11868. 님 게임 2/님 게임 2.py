# 백준 11868

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, stone):
    result = stone[0]
    for i in range(1, N):
        result ^= stone[i]

    return 'cubelover' if result == 0 else 'koosaga'


def main():
    N = int(input())
    stone = list(map(int, input().split()))

    print(solve(N, stone))


main()
