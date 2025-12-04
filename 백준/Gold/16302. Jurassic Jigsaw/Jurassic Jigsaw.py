# 백준 16302

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
    total = 0
    tree = []

    parent = [i for i in range(V+1)]
    edge.sort(key= lambda x: x[2])

    for cur in edge:
        startV, endV, cost = cur
        if find(parent, startV) != find(parent, endV):
            union(parent, startV, endV)
            total += cost
            tree.append([startV, endV])

    return [[total]] + tree


def solve(N, K, dna):
    edge = []
    for i in range(N-1):
        for j in range(i+1, N):
            diff = 0
            for k in range(K):
                if dna[i][k] != dna[j][k]:
                    diff += 1
            edge.append((i, j, diff))

    return Kruskal(N, edge)


def main():
    N, K = map(int, input().split())
    dna = []
    for _ in range(N):
        dna.append(input().decode().rstrip())
    
    for i in solve(N, K, dna):
        print(*i)


main()
