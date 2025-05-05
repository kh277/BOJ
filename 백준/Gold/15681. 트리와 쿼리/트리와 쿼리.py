# 백준 15681

import io, sys

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
sys.setrecursionlimit(10**6)


def treeDP(N, R, graph, visited, DP):
    leaf = 1

    for nextV in graph[R]:
        if visited[nextV] == False:
            visited[nextV] = True
            leaf += treeDP(N, nextV, graph, visited, DP)

    DP[R] = leaf
    return leaf


def main():
    N, R, Q = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(N-1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    DP = [0 for _ in range(N+1)]
    visited = [False for _ in range(N+1)]
    visited[R] = True
    treeDP(N, R, graph, visited, DP)
    for _ in range(Q):
        u = int(input())
        print(DP[u])


main()
