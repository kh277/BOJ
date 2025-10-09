# 백준 6497

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


def Kruskal(V, edge):
    totalCost = 0
    parent = [i for i in range(V)]
    edge.sort(key= lambda x: x[2])

    for cur in edge:
        startV, endV, cost = cur
        if find(parent, startV) != find(parent, endV):
            union(parent, startV, endV)
        else:
            totalCost += cost

    return totalCost


def main():
    while True:
        V, E = map(int, input().split())
        if V == 0:
            break
        edge = []
        for _ in range(E):
            edge.append(list(map(int, input().split())))
        print(Kruskal(V, edge))


main()
