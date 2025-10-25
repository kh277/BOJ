# 백준 25195

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def DFS(graph, fan):
    start = 1
    stack = array('I')
    stack.append(start)

    while stack:
        curV = stack.pop()

        if curV in fan:
            continue
        
        if len(graph[curV]) == 0:
            return 'yes'

        for nextV in graph[curV]:
            stack.append(nextV)

    return 'Yes'


def main():
    N, M = map(int, input().split())
    graph = [array('I') for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
    S = int(input())
    fan = set(map(int, input().split()))
    print(DFS(graph, fan))


main()
