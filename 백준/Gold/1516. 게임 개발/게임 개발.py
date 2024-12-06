# 백준 1516

'''
위상 정렬을 사용해 모든 건물을 짓는 데 걸리는 시간을 측정하자.
또한 현재 건물을 짓는 데 필요한 시간을 DP 테이블에 저장하면서 탐색한다.
'''

import sys
from collections import deque

input = sys.stdin.readline
INF = 10e8


def TopologySort(data):
    graph = [[] for _ in range(N+1)]
    inDegree = [0 for _ in range(N+1)]

    for i in data:
        graph[i[0]].append(i[1])
        inDegree[i[1]] += 1
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


def solve():
    # 해당 건물이 건설되었다면 건설된 시간 저장
    DP = [0 for _ in range(N+1)]
    graph, sequence = TopologySort(data)

    # 정렬된 순서에 따라 건설 시간 측정
    for curBuild in sequence:
        DP[curBuild] = DP[curBuild] + time[curBuild]
        for nextBuild in graph[curBuild]:
            DP[nextBuild] = max(DP[nextBuild], DP[curBuild])
    
    return DP[1:]


# main 함수 ----------
N = int(input())
data = []
inDegree = [0 for _ in range(N+1)]
time = [0 for _ in range(N+1)]

# 간선 저장
for i in range(1, N+1):
    t, *need = map(int, input().split())
    time[i] = t
    for j in need[:-1]:
        data.append([j, i])

print(*solve())
