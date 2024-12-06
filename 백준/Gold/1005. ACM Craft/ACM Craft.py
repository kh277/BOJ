# 백준 1005

'''
위상 정렬을 사용해 모든 건물을 짓는 데 걸리는 시간을 측정하자.
또한 현재 건물을 짓는 데 필요한 시간을 DP 테이블에 저장하면서 탐색한다.
'''

import sys
from collections import deque

input = sys.stdin.readline
INF = 10e8


def TopologySort():
    result = []
    q = deque()

    for i in range(1, N+1):
        if inDegree[i] == 0:
            q.append(i)

    while q:
        cur = q.popleft()
        result.append(cur)

        for neighbor in graph[cur]:
            inDegree[neighbor] -= 1

            if inDegree[neighbor] == 0:
                q.append(neighbor)

    return graph, result


def solve(W):
    # 해당 건물이 건설되었다면 건설된 시간 저장
    DP = [0 for _ in range(N+1)]
    graph, sequence = TopologySort()

    # 정렬된 순서에 따라 건설 시간 측정
    for curBuild in sequence:
        DP[curBuild] = DP[curBuild] + time[curBuild]
        for nextBuild in graph[curBuild]:
            DP[nextBuild] = max(DP[nextBuild], DP[curBuild])
    
    return DP[W]


# main 함수 ----------
T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    time = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(N+1)]
    inDegree = [0 for _ in range(N+1)]
    for _ in range(K):
        x, y = map(int, input().split())
        graph[x].append(y)
        inDegree[y] += 1
    W = int(input())
    print(solve(W))
