# 백준 21924

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])

    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    parent[max(a, b)] = min(a, b)


def kruskal(V, edge):
    totalCost = 0
    minCost = 0
    resultGraph = []

    parent = [i for i in range(V+1)]

    edge.sort(key= lambda x: x[2])

    # 우선순위 큐로 최소 비용 간선 연결
    for cur in edge:
        startV, endV, cost = cur
        totalCost += cost
        if find(parent, startV) != find(parent, endV):
            union(parent, startV, endV)
            minCost += cost
            resultGraph.append(cur)

    for i in range(1, V+1):
        parent[i] = find(parent, parent[i])

    # 모든 간선을 연결하는 MST가 존재하지 않는 경우 -1
    for i in range(1, V+1):
        if parent[i] != 1:
            return -1
    return totalCost - minCost


def main():
    N, M = map(int, input().split())
    edge = []
    for _ in range(M):
        edge.append(list(map(int, input().split())))
    print(kruskal(N, edge))


main()
