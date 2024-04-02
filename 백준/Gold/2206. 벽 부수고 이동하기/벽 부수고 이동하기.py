# 백준 2206

'''
벽을 한 번 부수고 이동할 수 있다.
따라서 벽을 부술 수 있는지 보여주는 bool 변수를 추가해서 x, y좌표와 함께 처리하면 된다.
벽에 마주치고 부술 수 있는 경우, bool 변수를 toggle 시키고 벽이 위치한 좌표를 큐에 넣으면 된다.

주의 반례 -> 시작점에서만 BFS를 진행하는 경우 목적지에 도달할 수 없음.
2 4
0111
0010
'''

import sys
from collections import deque

input = sys.stdin.readline


def BFS(M: int, N: int, graph: list, x: int, y: int, goalX: int, goalY: int) -> list:
    pointX = [-1, 1, 0, 0]
    pointY = [0, 0, -1, 1]
    visited = [[False for _ in range(M)] for _ in range(N)]

    q = deque()
    # [y좌표, x좌표, 움직인 칸 수, 벽을 뚫을 수 있는 횟수]
    q.append([y, x, 1, True])

    # 큐가 빌 때까지 반복
    while q:
        temp = q.popleft()

        # 상하좌우 탐색 가능한지 확인
        for i in range(4):
            nextY = temp[0] + pointY[i]
            nextX = temp[1] + pointX[i]

            # 탐색 가능한 경우
            if 0 <= nextX < M and 0 <= nextY < N and visited[nextY][nextX] == False:

                # 도착점에 도달한 경우
                if nextX == goalX and nextY == goalY:
                    return temp[2]+1

                # 벽을 아직 뚫지 않았고 벽을 만났을 때
                if temp[3] == True and graph[nextY][nextX] == '1':
                    visited[nextY][nextX] = True
                    q.append([nextY, nextX, temp[2]+1, False])

                # 벽이 아닌 곳을 만났을 때
                elif graph[nextY][nextX] == '0':
                    visited[nextY][nextX] = True
                    q.append([nextY, nextX, temp[2]+1, temp[3]])
                
    # 도달 불가능한 경우
    return -1


def solve(M: int, N: int, graph: list) -> int:

    # 예외 경우 - 격자가 1x1인 경우
    if M == 1 and N == 1:
        return 1
        
    # (0, 0)에서 탐색을 시작하는 경우
    start = BFS(M, N, graph[:], 0, 0, M-1, N-1)

    # (M-1, N-1)에서 탐색을 시작하는 경우
    end = BFS(M, N, graph[:], M-1, N-1, 0, 0)

    # 한 쪽에서 BFS를 시작하여 다른 끝쪽에 도달할 수 없는 경우 제거
    if start == -1 and end == -1:
        return -1
    elif start == -1 or end == -1:
        return max(start, end)
    else:
        return min(start, end)


def main():
    N, M = map(int, input().split())
    graph = []

    for i in range(N):
        graph.append(list(input().rstrip()))

    print(solve(M, N, graph))
    

main()