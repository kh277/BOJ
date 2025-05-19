# 백준 22858

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, K, S, D):
    before = S
    for _ in range(K):
        cur = array('I', [0]) * N
        for i in range(N):
            cur[D[i]-1] = before[i]
        before = cur

    return before


def main():
    N, K = map(int, input().split())
    S = list(map(int, input().split()))
    D = list(map(int, input().split()))
    print(*solve(N, K, S, D))


main()
