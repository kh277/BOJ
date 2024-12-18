# 백준 6936

'''
N개의 정점으로 이루어진 유향 그래프가 있을 때,
모든 원숭이가 각 정점에서 출발해서 원래의 정점으로 돌아오는 최소 횟수를 구하는 문제이다.
모든 정점은 나가는 간선 1개, 들어오는 간선 1개이다.
'''

import io
from collections import deque

input = io.BufferedReader(io.FileIO(0)).readline


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def DFS(start):
    visited = [False for _ in range(N+1)]
    
    q = deque()
    q.append([start, 0])
    visited[start] = True
    visitCount = 0

    while q:
        curNode, curDistance = q.pop()

        # 시작 정점을 재방문한 경우
        if curNode == start:
            visitCount += 1
            if visitCount == 2:
                return curDistance

        for nextNode in graph[curNode]:
            q.append([nextNode, curDistance+1])


def solve():
    distance = [0 for _ in range(N+1)]
    # 모든 정점에 대해 다시 돌아올 때까지 걸리는 시간 측정
    for i in range(1, N+1):
        distance[i] = DFS(i)
    
    # 모든 정점의 재방문 시간에 대한 최소공배수 구하기
    result = distance[1]
    for i in range(1, N+1):
        result = lcm(result, distance[i])

    return result


# main 함수 ----------
while True:
    N = int(input())
    if N == 0:
        break
    graph = [[] for _ in range(N+1)]
    for _ in range(N):
        a, b = map(int, input().split())
        graph[a].append(b)

    print(solve())