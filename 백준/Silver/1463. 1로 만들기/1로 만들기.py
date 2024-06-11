# 백준 1463

import sys

input = sys.stdin.readline


def solve(N: int) -> int:
    DP = [None for _ in range(N+1)]
    DP[0] = 0
    DP[1] = 0

    for i in range(2, N+1):
        DP[i] = DP[i-1]+1

        # 3으로 나눠 떨어지는 경우
        if i % 3 == 0:
            DP[i] = min(DP[i], DP[i//3]+1)
        
        # 2로 나눠 떨어지는 경우
        if i % 2 == 0:
            DP[i] = min(DP[i], DP[i//2]+1)
    
    return DP[N]


def main():
    N = int(input())

    print(solve(N))

main()
