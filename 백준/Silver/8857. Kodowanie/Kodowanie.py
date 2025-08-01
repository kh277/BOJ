# 백준 8857

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N):
    DP = [0 for _ in range(max(2, N))]
    DP[0] = 1
    DP[1] = 1
    
    for i in range(2, N):
        DP[i] = DP[i-1] + DP[i-2]
    
    return DP[N-1]


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(solve(N))


main()
