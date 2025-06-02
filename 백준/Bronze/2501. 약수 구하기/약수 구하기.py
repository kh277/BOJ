# 백준 2501

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, K):
    factors = []
    for i in range(1, N+1):
        if N % i == 0:
            factors.append(i)

    factors.sort()
    if K > len(factors):
        return 0
    return factors[K-1]


def main():
    N, K = map(int, input().split())
    print(solve(N, K))


main()
