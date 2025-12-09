# 백준 1833

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


def Kruskal(V, edge, prevCost):
    total = 0
    edgeMST = []
    parent = [i for i in range(V+1)]
    edge.sort(key= lambda x: x[2])

    for cur in edge:
        startV, endV, cost = cur
        if find(parent, startV) != find(parent, endV):
            union(parent, startV, endV)
            if cost != 0:
                total += cost
                edgeMST.append((startV, endV))

    return [[total+prevCost, len(edgeMST)]], edgeMST


def main():
    N = int(input())
    edge = []
    prevCost = 0
    for s in range(1, N+1):
        A = list(map(int, input().split()))
        for i in range(s, N):
            if A[i] > 0:
                edge.append((s, i+1, A[i]))
            elif A[i] < 0:
                edge.append((s, i+1, 0))
                prevCost -= A[i]
    for i in Kruskal(N, edge, prevCost):
        for j in i:
            print(*j)


main()
