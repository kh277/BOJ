# 백준 11725

'''
최종 부모 노드가 아닌 바로 자신의 부모 노드만 찾으면 되므로 BFS를 이용하여 탐색하자.
'''

import sys
from collections import deque

input = sys.stdin.readline


def BFS(V: int, graph: list, start: int) -> list:
    # 0번 정점은 사용하지 않음
    visited = [False for _ in range(V+1)]

    q = deque()
    q.append(start)
    visited[start] = start

    # 큐가 빌 때까지 반복
    while q:
        temp = q.popleft()

        # 이웃한 정점에 방문이 가능한지 확인
        for i in graph[temp]:
            if visited[i] != False:
                continue
            q.append(i)
            visited[i] = temp

    # 0번 정점은 사용하지 않고 1번 정점은 제외해야 하므로
    return visited[2:]


def main():
    N = int(input())

    E = [[] for i in range(N+1)]
    for i in range(N-1):
        a, b = map(int, input().split())
        E[a].append(b)
        E[b].append(a)
    
    for i in BFS(N, E, 1):
        print(i)
    

main()