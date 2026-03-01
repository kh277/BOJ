# 백준 17412

import io
from collections import deque
INF = 10000000

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


# BFS를 이용해 level 그래프 생성
def build(V, graph, source, sink, level):
    for i in range(V):
        level[i] = -1
    level[source] = 0
    q = deque()
    q.append(source)

    # source에서 각 정점까지 최단 거리를 level에 저장
    while q:
        curV = q.popleft()
        for nextV, cap, _ in graph[curV]:
            if cap > 0 and level[nextV] == -1:
                level[nextV] = level[curV] + 1
                q.append(nextV)

    return level[sink] != -1


# DFS를 이용해 차단 유량 계산
def findFlow(V, graph, level, pointer, source, sink):
    total = 0
    while True:
        stack = [(source, INF)]
        path = []
        foundFlow = 0

        # DFS 탐색
        while stack:
            curV, curFlow = stack[-1]
            # sink에 도달한 경우 종료
            if curV == sink:
                foundFlow = curFlow
                break

            isPushed = False
            for i in range(pointer[curV], len(graph[curV])):
                nextV, cap, revV = graph[curV][i]

                # 레벨+1 정점으로만 이동
                if cap > 0 and level[curV] < level[nextV]:
                    stack.append((nextV, min(curFlow, cap)))
                    path.append((curV, i))
                    pointer[curV] = i
                    isPushed = True
                    break
                pointer[curV] += 1

            # 더 이동할 수 없는 경우
            if isPushed == False:
                stack.pop()
                if path:
                    path.pop()
                level[curV] = -1

        if foundFlow == 0:
            break
        
        # 잔여 용량 갱신
        for curV, index in path:
            nextV, cap, revV = graph[curV][index]
            graph[curV][index][1] -= foundFlow
            graph[nextV][revV][1] += foundFlow

        total += foundFlow

    return total


def Dinic(V, graph, source, sink):
    maxFlow = 0
    level = [-1] * V

    # level 그래프를 구성할 수 없을 때까지 반복
    while build(V, graph, source, sink, level):
        pointer = [0] * V
        maxFlow += findFlow(V, graph, level, pointer, source, sink)

    return maxFlow


def main():
    V, E = map(int, input().split())

    # 그래프 작성 (graph[startV] = [[endV, capacity, reverseI], ...])
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        s, e = map(int, input().split())
        s -= 1
        e -= 1
        graph[s].append([e, 1, len(graph[e])])
        graph[e].append([s, 0, len(graph[s])-1])

    print(Dinic(V, graph, 0, 1))


main()
