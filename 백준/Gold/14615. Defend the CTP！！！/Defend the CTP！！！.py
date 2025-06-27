# 백준 14615

'''
1번 정점 -> C번 정점 -> N번 정점 으로 가는 경로가 있는지를 체크해야 한다.
1번 정점에서 정방향 간선으로 접근할 수 있는 정점을 전부 구해두고,
N번 정점에서 역방향 간선으로 접근할 수 있는 정점을 전부 구해둔다.
두 방향 모두 C번 정점을 접근할 수 있으면 경로가 존재한다고 볼 수 있다.
'''

import io
from array import array
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def BFS(N, start, edge):
    q = deque()
    q.append(start)
    visited = bytearray(N+1)
    visited[start] ^= 1

    while q:
        curV = q.popleft()

        for nextV in edge[curV]:
            if visited[nextV] == 0:
                q.append(nextV)
                visited[nextV] ^= 1
    
    return visited


def main():
    N, M = map(int, input().split())
    edge = [array('I') for _ in range(N+1)]
    revEdge = [array('I') for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        edge[a].append(b)
        revEdge[b].append(a)

    startVisit = BFS(N, 1, edge)
    endVisit = BFS(N, N, revEdge)

    T = int(input())
    for _ in range(T):
        C = int(input())
        if startVisit[C] & endVisit[C] == 1:
            print("Defend the CTP")
        else:
            print("Destroyed the CTP")


main()
