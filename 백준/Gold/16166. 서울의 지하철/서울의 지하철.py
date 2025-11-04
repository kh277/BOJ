# 백준 16166

import io
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def BFS(N, graph, target):
    start = 0

    # 서울역과 이어진 역이 없는 경우
    if start not in graph:
        return -1

    q = deque()
    visited = dict()
    for i in graph[start]:
        q.append(i)
        visited[i[0]] = 0

    while q:
        curV, curL = q.popleft()
        curMove = visited[curV]

        for nextV, nextL in graph[curV]:
            # 환승 여부 처리
            isMoved = 0
            if curL != nextL:
                isMoved = 1

            # 다음 정점이 방문했던 정점이고 갱신이 된다면
            if nextV in visited and visited[nextV] > visited[curV]+isMoved:
                visited[nextV] = curMove + isMoved
                q.append((nextV, nextL))
            # 다음 정점이 방문하지 않은 정점이라면
            elif nextV not in visited:
                visited[nextV] = curMove + isMoved
                q.append((nextV, nextL))

    if target not in visited:
        return -1
    return visited[target]


def main():
    N = int(input())
    graph = dict()
    for i in range(N):
        a, *L = list(map(int, input().split()))
        if a == 1:
            if L[0] in graph:
                graph[L[0]].append((L[0], i))
            else:
                graph[L[0]] = [(L[0], i)]
        for j in range(1, a):
            if L[j-1] in graph:
                graph[L[j-1]].append((L[j], i))
            else:
                graph[L[j-1]] = [(L[j], i)]
            if L[j] in graph:
                graph[L[j]].append((L[j-1], i))
            else:
                graph[L[j]] = [(L[j-1], i)]
    target = int(input())

    print(BFS(N, graph, target))


main()
