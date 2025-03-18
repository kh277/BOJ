# 백준 32753

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, K):
    if N == 1:
        return [1 for _ in range(K)]
    
    if N == 2 and K == 1:
        return [1, 2]
    
    return [-1]


def main():
    N, K = map(int, input().split())
    print(*solve(N, K))


main()