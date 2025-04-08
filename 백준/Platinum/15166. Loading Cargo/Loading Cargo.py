# 백준 15166

'''
BFS를 통해 이분 그래프를 구하여 각 부분 별 정점의 개수를 순서쌍으로 저장한다.
그 뒤, DP를 통해 왼쪽 방과 오른쪽 방에 들어갈 수 있는 지 여부를 처리해주면 된다.

DP[i][sumL] = i번째 순서쌍까지 고려하고, 왼쪽 방에 들어있는 캡슐의 수가 sumL일 때 오른쪽 방에 들어있는 캡슐의 수
'''

import io
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**4


def BFS(start, graph, visited):
    q = deque()
    q.append([start, 0])
    visited[start] = 0
    typeNum = [1, 0]

    while q:
        curV, curType = q.popleft()
        for nextV in graph[curV]:
            if visited[nextV] == -1:
                q.append([nextV, curType^1])
                visited[nextV] = curType^1
                typeNum[curType^1] += 1
            else:
                if visited[nextV] == curType:
                    return [-1, -1]

    return typeNum


def solve(L, R, N, graph):
    # 저장고가 0일 때
    if L == 0 and R == 0:
        if N == 0:
            return 'Yes'
        return 'No'

    # 이분 그래프의 구성 정점 개수 반환
    capsule = []
    visited = [-1 for _ in range(N)]
    for i in range(N):
        if visited[i] == -1:
            a, b = BFS(i, graph, visited)
            if a == -1:
                return 'No'
            capsule.append([a, b])

    # DP 초기값 설정
    DP = [[INF for _ in range(L+1)] for _ in range(len(capsule))]
    if capsule[0][0] <= L:
        DP[0][capsule[0][0]] = capsule[0][1]
    if capsule[0][1] <= L:
        DP[0][capsule[0][1]] = capsule[0][0]

    # DP 처리
    for i in range(1, len(capsule)):
        curA, curB = capsule[i]
        for sumL in range(L+1):
            if sumL - curA >= 0 and DP[i-1][sumL-curA] != INF:
                DP[i][sumL] = min(DP[i][sumL], DP[i-1][sumL-curA]+curB)
            if sumL - curB >= 0 and DP[i-1][sumL-curB] != INF:
                DP[i][sumL] = min(DP[i][sumL], DP[i-1][sumL-curB]+curA)

    # R의 저장용량을 넘지 않는 경우가 존재하는지 확인
    for i in range(L+1):
        if DP[len(capsule)-1][i] <= R:
            return 'Yes'
    return 'No'


def main():
    L, R, N, C = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(C):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    print(solve(L, R, N, graph))


main()
