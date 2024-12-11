# 백준 2133

'''
i번째는 (i-2번째까지의 경우) * (2칸짜리 모양이 가능한 경우 3가지)
+ (i-4번째 까지의 경우) * (4칸짜리 모양이 가능한 경우 2가지)
+ ...
가 된다.
'''

import sys

input = sys.stdin.readline

def solve():
    DP = [0 for _ in range(max(5, N+1))]
    DP[2] = 3
    DP[4] = 11

    for i in range(6, N+1, 2):
        DP[i] = 4*DP[i-2] - DP[i-4]

    return DP[N]


# main 함수 ----------
N = int(input())
print(solve())