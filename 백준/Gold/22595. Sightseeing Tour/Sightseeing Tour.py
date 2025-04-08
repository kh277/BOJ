# 백준 22595

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, graph):
    minCost = 0
    for i in range(N):
        for j in range(i+1, N):
            minCost += min(graph[i][j], graph[j][i])
    
    return minCost


def main():
    N = int(input())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))
    print(solve(N, graph))


main()
