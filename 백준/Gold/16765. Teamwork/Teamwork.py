# 백준 16765

'''
DP[i] = i번째 소까지 팀을 구성했을 때, 얻을 수 있는 스킬 레벨 합의 최대값
'''

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, K, cow):
    DP = array('i', [0]) * N

    # DP 초기값 계산
    maxV = 0
    for cur in range(K):
        maxV = max(maxV, cow[cur])
        DP[cur] = maxV*(cur+1)

    # 이후 DP 계산
    for cur in range(K, N):
        maxV = 0
        for size in range(1, K+1):
            prev = cur - size
            maxV = max(maxV, cow[prev+1])
            DP[cur] = max(DP[cur], DP[prev] + maxV*size)

    return DP[N-1]


def main():
    N, K = map(int, input().split())
    cow = array('i') * N
    for _ in range(N):
        cow.append(int(input()))
    print(solve(N, K, cow))


main()
