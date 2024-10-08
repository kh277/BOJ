# 백준 30460

'''
DP[i] = i초가 지났을 때, 얻을 수 있는 점수의 최대값
'''

import sys

input = sys.stdin.readline

def solve():
    DP = [0 for _ in range(N)]
    DP[0] = A[0]
    DP[1] = A[0]+A[1]
    DP[2] = max(A[0]+A[1]+A[2], 2*(A[0]+A[1]+A[2]))

    for i in range(3, N):
        DP[i] = max(DP[i-3]+2*(A[i-2]+A[i-1]+A[i]), DP[i-2]+A[i-1]+A[i], DP[i-1]+A[i])
    
    return max(DP[N-1], DP[N-3]+2*(A[N-2]+A[N-1]), DP[N-2]+2*A[N-1])



# main 함수 ----------
N = int(input())
A = list(map(int, input().split()))

print(solve())