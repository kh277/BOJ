# 백준 14907

import io
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def TopologySort(V, graph, inDegree):
    seq = []
    q = deque()

    for i in range(V):
        if inDegree[i] == 0:
            q.append(i)

    while q:
        cur = q.popleft()
        seq.append(cur)

        for neighbor in graph[cur]:
            inDegree[neighbor] -= 1

            if inDegree[neighbor] == 0:
                q.append(neighbor)

    return seq


def solve(V, graph, inDegree, time):
    # 위상 정렬 수행
    seq = TopologySort(V, graph, inDegree)

    # seq 순서대로 작업 수행 및 DP로 최소 시간 측정
    DP = [0 for _ in range(V)]
    for curV in seq:
        DP[curV] = DP[curV] + time[curV]
        for nextV in graph[curV]:
            DP[nextV] = max(DP[nextV], DP[curV])

    return max(DP)


def main():
    N = 26
    graph = [[] for _ in range(N)]
    inDegree = [0 for _ in range(N)]
    time = [0 for _ in range(N)]
    while True:
        try:
            a = list(input().decode().split())
            nextV = ord(a[0])-65
            time[nextV] = int(a[1])
            if len(a) == 3:
                inDegree[nextV] += len(a[2])
                for i in a[2]:
                    graph[ord(i)-65].append(nextV)
        except:
            break

    print(solve(N, graph, inDegree, time))


main()
