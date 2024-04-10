# 백준 2606

'''
웜 바이러스에 걸린 컴퓨터를 시작점으로 잡아 BFS를 진행한다.

주의 반례 -> 컴퓨터가 1대만 존재하는 경우
1
0
'''

import sys
from collections import deque

input = sys.stdin.readline


def BFS(V: int, E: int, graph: list, start: int) -> list:
    visited = [False for _ in range(V+1)]

    q = deque()
    q.append(start)

    # 큐가 빌 때까지 반복
    while q:
        temp = q.popleft()
        visited[temp] = True

        # 이웃한 정점에 방문이 가능한지 확인
        for i in graph[temp]:
            if visited[i] == True:
                continue
            q.append(i)

    return len([x for x in range(V+1) if visited[x] == True])


def main():
    V = int(input())
    E = int(input())

    graph = [[] for _ in range(V+1)]
    for i in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    # 1번 컴퓨터를 통해 걸린 컴퓨터 수를 구하는 것이므로 -1 하기
    print(BFS(V, E, graph, 1) - 1)

main()