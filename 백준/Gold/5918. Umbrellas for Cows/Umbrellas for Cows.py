# 백준 5918

'''
DP[i] = 1 ~ i번째 소까지 덮는데 필요한 최소 비용
좌표 기준으로 탐색하면 O(NM)이 되어 시간초과가 발생하게 된다.
따라서 소를 기준으로 탐색한다면 O(N^2)으로 탐색할 수 있게 된다.
'''

import sys

input = sys.stdin.readline


def solve():
    # 큰 우산이 더 싼 경우를 처리하기 위해 우산 가격 증가순 처리
    for i in range(M-1, -1, -1):
        cost[i] = min(cost[i], cost[i+1])

    # DP 초기화 : 1번 소 ~ i번 소까지 전부 덮을 때 필요한 값으로 초기화
    DP = [cost[cows[i]-cows[0]+1] for i in range(N)]

    # DP 계산
    for i in range(1, N):     # 현재 탐색하는 소의 번호
        for j in range(1, i+1):    # 비교할 이전 소의 번호
            umbrellaSize = cows[i] - cows[j] + 1
            DP[i] = min(DP[i], DP[j-1]+cost[umbrellaSize])

    return DP[N-1]


# main 함수 ----------
N, M = map(int, input().split())
cows = []
for _ in range(N):
    cows.append(int(input()))
cows.sort()

cost = [0]
for _ in range(M):
    cost.append(int(input()))

print(solve())