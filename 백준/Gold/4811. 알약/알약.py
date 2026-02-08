# 백준 4811

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, DP, cal):
    if cal >= N:
        return DP[N]
    
    for i in range(cal+1, N+1):
        for j in range(i):
            DP[i] += DP[j] * DP[i-j-1]
    
    return DP[N]


def main():
    DP = [0 for _ in range(31)]
    DP[0] = 1
    DP[1] = 1
    cal = 1
    while True:
        N = int(input())
        if N == 0:
            break
        print(solve(N, DP, cal))
        cal = max(cal, N)


main()
