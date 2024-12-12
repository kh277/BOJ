# 백준 1029

'''
현재까지 거래한 사람들의 집합을 비트마스킹으로 처리하고, 바텀업DP로 최적화하자.

DP[i][status] = 현재 그림을 i가 소유하고 있고, status에 해당하는 사람이 소유한 적이 있을 때,
해당 status까지 도달한 경우 그림의 최소값.
'''

import sys

input = sys.stdin.readline
INF = 10


def recur(status, curOwner, curPrice, DP):
    # 갱신할 필요가 없는 경우
    if DP[curOwner][status] <= curPrice:
        if DP[curOwner][status] != INF:
            return 

    # 재귀
    for nextOwner in range(2, N+1):
        # 그림을 소유한 적이 없고, curPrice 이상으로 산다면
        if not status & (1 << nextOwner) and price[curOwner][nextOwner] >= curPrice:
            recur(status | (1 << nextOwner), nextOwner, price[curOwner][nextOwner], DP)

    DP[curOwner][status] = min(curPrice, DP[curOwner][status])
    return


def solve():
    DP = [[INF for _ in range(2**(N+1))] for _ in range(N+1)]

    # 외부 상인에게서 1번 아티스트가 구매
    status = 1 | (1 << 1)

    # 재귀로 이후 과정 탐색
    recur(status, 1, 0, DP)

    # DP 값이 저장되어 있는 경우, 소유한 아티스트의 수 체크
    maxCount = 0
    for i in range(N+1):
        for j in range(2**(N+1)):
            if DP[i][j] != INF:
                temp = 0
                for k in range(1, N+1):
                    if j & (1 << k):
                        temp += 1
                maxCount = max(maxCount, temp)
    
    return maxCount


# main 함수 ----------
N = int(input())
price = [[0]*(N+1)]
for _ in range(N):
    price.append([0] + list(map(int, input().rstrip())))

print(solve())