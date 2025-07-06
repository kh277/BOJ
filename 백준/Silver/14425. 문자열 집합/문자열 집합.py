# 백준 14225

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def main():
    N, M = map(int, input().split())
    S = set()
    for _ in range(N):
        S.add(input().decode().rstrip())
    count = 0
    for _ in range(M):
        if input().decode().rstrip() in S:
            count += 1

    print(count)


main()
