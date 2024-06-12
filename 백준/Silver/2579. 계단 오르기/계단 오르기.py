# 백준 2579

'''
DP[i] = i번째 계단까지 올라갔을 때 점수의 최대값
'''

import sys

input = sys.stdin.readline


def solve(N: int, score: list) -> int:
    DP = [0 for _ in range(N+1)]
    DP[1] = score[1]

    # N == 1인 경우
    if N == 1:
        return DP[1]

    # N이 2보다 큰 경우
    DP[2] = score[1]+score[2]

    for i in range(3, N+1):
        DP[i] = max(DP[i-2]+score[i], DP[i-3]+score[i-1]+score[i])
        
    
    return DP[N]


def main():
    N = int(input())
    score = [0]
    for i in range(N):
        score.append(int(input()))

    print(solve(N, score))


main()
