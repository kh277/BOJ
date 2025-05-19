# 백준 22858

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(graph):
    for curV in range(12):
        if len(graph[curV]) == 3:
            size = set()
            for nextV in graph[curV]:
                size.add(len(graph[nextV]))
            if len(size) == 3:
                return curV+1


def main():
    graph = [[] for _ in range(12)]
    for _ in range(12):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)

    print(solve(graph))


main()
