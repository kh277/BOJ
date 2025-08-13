# 백준 1764

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(hear, see):
    result = sorted(hear & see)
    return [len(result)] + sorted(result)


def main():
    N, M = map(int, input().split())
    hear = set()
    see = set()
    for _ in range(N):
        hear.add(input().decode().rstrip())
    for _ in range(M):
        see.add(input().decode().rstrip())

    for i in solve(hear, see):
        print(i)


main()
