# 백준 11502

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(S):
    size = 0
    for i in range(len(S)):
        for j in range(2, len(S)+1-i, 2):
            if sum(S[i:i+j//2]) == sum(S[i+j//2:i+j]):
                size = max(size, j)

    return size


def main():
    N = list(map(int, input().decode().strip()))
    print(solve(N))


main()
