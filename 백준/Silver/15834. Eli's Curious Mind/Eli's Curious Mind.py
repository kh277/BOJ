# 백준 15834

'''
DP[i] = i번째 시험관의 물질을 혼합물에 사용하는 경우, 만들 수 있는 혼합물의 수.
'''

import sys

input = sys.stdin.readline


def solve():
    # 혼합물은 2가지 이상을 섞어야 하므로 N<3일 경우는 0 리턴
    if N == 1 or N == 2:
        return 0

    # N=3일 때까지는 DP 처리에서 예외이므로
    if N == 3:
        return 1
    
    DP = [0 for _ in range(max(N+1, 5))]

    # 초기값 설정
    DP[0] = 0
    DP[1] = 1
    DP[2] = 1
    DP[3] = 1

    # DP 계산
    for i in range(4, N+1):
        DP[i] = DP[i-2] + DP[i-3]
    
    return DP[N] + DP[N-1]


# main 함수 ----------
index = 1
while True:
    N = int(input())
    if N == 0:
        break
    print("Case #{a}: {b}".format(a=index, b=solve()))
    index += 1