# 백준 32942

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve():
    graph = [set() for _ in range(11)]
    for x in range(1, 11):
        for y in range(1, 11):
            if A*x + B*y == C:
                graph[x].add(y)

    return [[0] if len(i) == 0 else sorted(list(i)) for i in graph[1:]]


# main 함수 ----------
A, B, C = map(int, input().split())

for i in solve():
    print(*i)
