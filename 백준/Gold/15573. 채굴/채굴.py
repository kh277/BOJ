# 백준 15573

'''
이분 탐색으로 채굴기의 성능 D를 정해 광물을 채굴할 수 있는지 판단한다.
'''

import sys
from collections import deque

input = sys.stdin.readline


def BFS(x: int):
    pointX = [-1, 1, 0, 0]
    pointY = [0, 0, -1, 1]
    visited = [[False for _ in range(M)] for _ in range(N)]
    result = 0       # 캘 수 있는 광물 개수 저장
    
    # 강도가 x 이하인 모서리 광물 start에 추가
    start = []
    for i in range(N):
        if data[i][0] <= x:
            start.append([i, 0])
            visited[i][0] = True
            result += 1
        if data[i][M-1] <= x:
            start.append([i, M-1])
            visited[i][M-1] = True
            result += 1
    for i in range(1, M-1):
        if data[0][i] <= x:
            start.append([0, i])
            visited[0][i] = True
            result += 1
    
    q = deque()
    for i in start:
        q.append(i)
    
    while q:
        curY, curX = q.popleft()
        
        for i in range(4):
            nextX = curX + pointX[i]
            nextY = curY + pointY[i]
            
            if 0 <= nextX < M and 0 <= nextY < N and visited[nextY][nextX] == False:
                if data[nextY][nextX] <= x:
                    q.append([nextY, nextX])
                    visited[nextY][nextX] = True
                    result += 1

    return result


def solve():
    start = 1
    end = 1000000
    
    while True:
        # 종료조건
        if end - start == 1:
            if BFS(start) >= K:
                return start
            else:
                return end
        
        # 결정 문제 및 이분 탐색
        mid = (start+end)//2
        cur_mining = BFS(mid)
        
        if cur_mining < K:
            start = mid
        else:
            end = mid


# main 함수 ----------
N, M, K = map(int, input().split())

data = []
for _ in range(N):
    data.append(list(map(int, input().split())))

print(solve())