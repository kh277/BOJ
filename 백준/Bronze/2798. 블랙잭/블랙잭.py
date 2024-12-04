# 백준 2798

import sys

input = sys.stdin.readline


def solve():
    result = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                cur = card[i] + card[j] + card[k]
                if cur <= M and cur > result:
                    result = cur
    
    return result


# main 함수 ----------
N, M = map(int, input().split())
card = list(map(int, input().split()))
print(solve())
