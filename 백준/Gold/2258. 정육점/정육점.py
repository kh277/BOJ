# 백준 2258

'''
1. 고기 하나 + 해당 고기보다 싼 고기 전부 덤
2. 같은 가격 고기 여러 개 + 해당 고기보다 싼 고기 전부 덤
두 가지 케이스를 전부 고려해야 한다.
따라서 비용이 커지도록, 같은 비용이라면 무게가 줄어들도록 고기를 훑으면서, 현재 무게가 M 이상이라면 현재 비용과 최소 비용을 비교해주면 된다. 
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**10


def solve(N, M, cost):
    minCost = INF
    accW = 0
    for curC in sorted(cost.keys()):
        accC = 0
        for curW in sorted(cost[curC], reverse=True):
            accW += curW
            accC += curC

            if accW >= M:
                minCost = min(minCost, accC)

    return -1 if minCost == INF else minCost


def main():
    N, M = map(int, input().split())
    cost = dict()
    for _ in range(N):
        a, b = map(int, input().split())
        if b in cost:
            cost[b].append(a)
        else:
            cost[b] = [a]

    print(solve(N+1, M, cost))


main()
