# 백준 28119

'''
N개의 정점에서 회의가 열리므로, 결국 모든 정점을 방문해야 한다.
따라서 N-1개의 간선을 우선순위 큐에서 뽑는 MST를 구하면 된다.
시작 정점과 다시 돌아와야 한다는 조건은 신경쓰지 않아도 된다.
'''

import io, sys

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
sys.setrecursionlimit(10**5)


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])

    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    parent[max(a, b)] = min(a, b)


def Kruskal(V, edge):
    totalCost = 0
    resultGraph = []
    parent = [i for i in range(V+1)]

    edge.sort(key= lambda x: x[2])
    for cur in edge:
        startV, endV, cost = cur
        if find(parent, startV) != find(parent, endV):
            union(parent, startV, endV)
            totalCost += cost
            resultGraph.append(cur)

    return totalCost


def main():
    N, M, S = map(int, input().split())
    edge = []
    for _ in range(M):
        edge.append(list(map(int, input().split())))

    print(Kruskal(N, edge))


main()
