# 백준 14948

'''
현재의 레벨을 K라고 하면,
BFS를 통해 시작점에서 도착점까지 도착할 수 있는지를 확인한다.

위 과정을 이분 탐색을 통해 반복하여 최소값을 구하자. 
'''

import sys
from collections import deque

input = sys.stdin.readline

def BFS(limit):
    pointX = [-1, 1, 0, 0]
    pointY = [0, 0, -1, 1]

    # 0 = 특수장비를 사용하고 방문, 1 = 특수장비를 사용하지 않고 방문, 2 = 미방문
    visited = [[2 for _ in range(M)] for _ in range(N)]
    
    q = deque()
    if graph[0][0] <= limit:
        q.append([0, 0, 1])     # [y좌표, x좌표, 남은 특수장비 사용 횟수]
        visited[0][0] = 1

    while q:
        curY, curX, leftCount = q.popleft()
        
        # 출구에 도달한 경우
        if curY == N-1 and curX == M-1:
            return True

        # 상하좌우
        for i in range(4):
            nextX = curX + pointX[i]
            nextY = curY + pointY[i]

            if 0 <= nextX < M and 0 <= nextY < N:
                # 방문할 지점이 미방문이거나, 특수장비를 사용하여 먼저 방문한 경우(0) 방문 가능
                if visited[nextY][nextX] == 2 or (visited[nextY][nextX] == 0 and leftCount == 1):
                    # 레벨이 낮아 넘지 못하는 경우
                    if graph[nextY][nextX] > limit:
                        # 특수장비 사용
                        if leftCount == 1:
                            nextX = nextX + pointX[i]
                            nextY = nextY + pointY[i]
                            # 건너뛸 곳이 미방문이고 레벨이 충분한 경우만 방문 가능
                            if 0 <= nextX < M and 0 <= nextY < N and visited[nextY][nextX] == 2:
                                if graph[nextY][nextX] <= limit:
                                    q.append([nextY, nextX, leftCount-1])
                                    visited[nextY][nextX] = 0
                    
                    # 레벨이 충분한 경우
                    else:
                        q.append([nextY, nextX, leftCount])
                        visited[nextY][nextX] = leftCount

    # 출구에 도달하지 못한 경우
    return False


def solve():
    start = 0
    end = 1000000000

    # 이분 탐색
    while end - start > 1:
        mid = (start+end)//2

        if BFS(mid) == True:
            end = mid
        else:
            start = mid
    
    if BFS(start) == True:
        return start
    else:
        return end


# main 함수 ----------
N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

print(solve())