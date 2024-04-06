# 백준 14052

'''
연구소의 최대 크기는 8*8이다.
브루트포스로 벽을 세울 위치를 계산할 경우,
벽을 최대 3개 세울 수 있으므로 64*63*62가지를 따져 봐야 한다.
해당 위치에 벽이 생겼다고 가정했을 때 BFS를 진행해서 안전 영역의 크기를 구해야 한다. O(N^2).
따라서 최악의 경우 64*63*62*8*8 = 약 1500만 만큼의 연산이 필요하다.
따라서 1초 내에 수행이 가능하다.

주의 반례
4 4
2 1 0 0
1 0 0 0
0 0 0 1
0 0 1 2
'''

import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline


def BFS(M: int, N: int, graph: list, start: list, wall: list) -> list:
    pointX = [-1, 1, 0, 0]
    pointY = [0, 0, -1, 1]

    # 벽으로 지정한 부분은 1로 설정
    for i in wall:
        if graph[i[0]][i[1]] == 1 or graph[i[0]][i[1]] == 2:
            return 0
        graph[i[0]][i[1]] = 1

    # 바이러스의 위치를 시작 위치로 설정
    q = deque()

    for i in start:
        q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        temp = q.popleft()

        # 상하좌우 탐색 가능한지 확인
        for i in range(4):
            nextY = temp[0] + pointY[i]
            nextX = temp[1] + pointX[i]

            # 탐색 가능한 경우 큐에 넣고 graph에 표시
            if 0 <= nextX < M and 0 <= nextY < N and graph[nextY][nextX] == 0:
                graph[nextY][nextX] = 2
                q.append([nextY, nextX])
    
    # 안전 영역의 크기 확인
    result = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                result += 1

    return result


def solve(M: int, N: int, graph: list) -> int:
    maximum = 0
    virus = []

    # 바이러스의 위치를 미리 파악해준다
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 2:
                virus.append([i, j])
    
    # 벽이 들어갈 수 있는 위치를 브루트포스로 설정
    for i in range(N*M-2):
        for j in range(i+1, N*M-1):
            for k in range(j+1, N*M):
                # 탐색을 시작할 바이러스의 위치와 벽의 위치를 [행, 열]로 전달함
                temp = BFS(M, N, deepcopy(graph), virus, [[i//M, i%M], [j//M, j%M], [k//M, k%M]])

                if maximum < temp:
                    maximum = temp

    return maximum


def main():
    N, M = map(int, input().split())
    graph = []
    for i in range(N):
        graph.append(list(map(int, input().split())))
    
    print(solve(M, N, graph))


main()
