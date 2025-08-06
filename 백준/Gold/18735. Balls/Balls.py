# 백준 18735

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, C):
    if N == 1:
        return 1

    result = set()
    for i in range(1, N):
        if C[i-1] == C[i]:
            result.add(C[i])
    for i in range(2, N):
        if C[i-2] == C[i]:
            result.add(C[i])

    return len(result)


def main():
    N = int(input())
    C = list(map(int, input().split()))
    print(solve(N, C))


main()
