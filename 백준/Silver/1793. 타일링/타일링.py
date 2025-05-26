# 백준 1793

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
DP = [-1] * 251
DP[0] = 1
DP[1] = 1
DP[2] = 3
last = 3


def solve(N):
    if DP[N] != -1:
        return DP[N]
    
    for i in range(last, N+1):
        DP[i] = DP[i-1] + 2*DP[i-2]
    
    return DP[N]


def main():
    while True:
        try:
            N = int(input())
            print(solve(N))
        except:
            break


main()
