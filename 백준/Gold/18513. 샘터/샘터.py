# 백준 18513

'''
각 샘터에서 가장 가까운 곳에 설치해야 하므로 BFS로 탐색하자.
'''

import sys
from collections import deque

input = sys.stdin.readline


# BFS : 연못의 위치를 시작지점으로 K번만큼 BFS 탐색 
def BFS(K):
    visited = set()
    pointX = [-1, 1]
    result = 0

    q = deque()
    for i in range(N):
        q.append([pond[i], 0])     # [좌표, 거리] 순으로 저장
        visited.add(pond[i])

    while True:
        curX, curDist = q.popleft()

        for i in range(2):
            nextX = curX + pointX[i]

            if K == 0:
                return result

            if nextX not in visited:
                q.append([nextX, curDist+1])
                visited.add(nextX)
                result += curDist+1
                K -= 1


# main 함수 ----------
N, K = map(int, input().split())
pond = list(map(int, input().split()))
print(BFS(K))