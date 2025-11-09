# 백준 16435

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, L, A):
    A.sort()
    cur = L
    for i in range(N):
        if A[i] > cur:
            return cur
        cur += 1
    return cur


def main():
    N, L = map(int, input().split())
    A = list(map(int, input().split()))
    print(solve(N, L, A))


main()
