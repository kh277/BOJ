# 백준 1795


import sys
from collections import deque

input = sys.stdin.readline


def BFS(start: list, check: list):
    malMove = start[2]-1       # 연속으로 이동할 수 있는 횟수이므로 K-1이 되어야 함.
    pointX = [1, 2, 2, 1, -1, -2, -2, -1]
    pointY = [-2, -1, 1, 2, 2, 1, -1, -2]
    visited = [[False for _ in range(M)] for _ in range(N)]
    
    # 큐에는 [y, x, 남은 연속 이동 가능 횟수, 총 이동한 횟수] 순서로 저장
    q = deque()
    q.append([start[0], start[1], start[2], 1])
    visited[start[0]][start[1]] = True
    check[start[0]][start[1]][1] += 1

    while q:
        curY, curX, canMove, curMove = q.popleft()

        for i in range(8):
            nextX = curX + pointX[i]
            nextY = curY + pointY[i]
            
            # 범위 내이고 방문하지 않았다면
            if 0 <= nextX < M and 0 <= nextY < N and visited[nextY][nextX] == False:
                # 연속 이동 횟수를 다 사용한 경우
                if canMove == 0:
                    q.append([nextY, nextX, malMove, curMove+1])
                    check[nextY][nextX][0] += curMove+1
                # 연속 이동 횟수가 아직 남은 경우
                else:
                    q.append([nextY, nextX, canMove-1, curMove])
                    check[nextY][nextX][0] += curMove
                visited[nextY][nextX] = True
                check[nextY][nextX][1] += 1


def solve():
    # 마알의 위치 저장, [y, x, 마알의 연속 이동 가능 수]
    pos = []
    for y in range(N):
        for x in range(M):
            if graph[y][x] != '.':
                pos.append([y, x, int(graph[y][x])])
    
    # [모든 마알의 누적 이동 횟수, 해당 칸을 방문한 마알의 수] 저장
    check = [[[0, 0] for _ in range(M)] for _ in range(N)]
    
    # BFS를 통해 마알이 방문할 수 있는 칸 탐색
    for i in pos:
        BFS(i, check)
    
    # 마알이 방문할 수 있는 칸 중 가장 작은 값 반환 
    result = 1000
    for y in range(N):
        for x in range(M):
            if check[y][x][1] == len(pos):
                result = min(result, check[y][x][0])
    
    return result if result != 1000 else -1


# main 함수 ----------
N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(input().rstrip()))

print(solve())