# 백준 25706

import sys

input = sys.stdin.readline


def solve(N: int, num: list) -> list:
    DP = [[] for _ in range(N)]
    
    DP[N-1] = 1
    for i in range(N-2, -1, -1):
        if num[i] == 0:
            DP[i] = 1 + DP[i+1]
        else:
            # N을 넘어가버리는 경우
            if i + num[i] >= N-1:
                DP[i] = 1
            else:
                DP[i] = 1+ DP[i+num[i]+1]
    
    return DP


def main():
    N = int(input())
    num = list(map(int, input().split()))
    
    print(*solve(N, num))


main()