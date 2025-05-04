# 백준 17352

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


def solve(N, edge):
    parent = [i for i in range(N+1)]
    for curS, curE in edge:
        if find(parent, curS) != find(parent, curE):
            union(parent, curS, curE)

    for i in range(1, N+1):
        parent[i] = find(parent, parent[i])

    cand = list(set(parent[1:]))
    return [cand[0], cand[1]]


def main():
    N = int(input())
    edge = []
    for _ in range(N-2):
        edge.append(list(map(int, input().split())))

    print(*solve(N, edge))


main()
