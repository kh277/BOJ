# 백준 25478

'''
N * M 크기의 격자에서 U에서 시작한 뒤 N을 전부 먹고 I에 도달하는 최단 거리를 구하는 문제이다.
격자에서 점 간 거리를 구한 뒤, 외판원 순회처럼 풀면 된다. 
'''

import io
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**6
pointX = [-1, 1, 0, 0]
pointY = [0, 0, -1, 1]


# start에서 다른 모든 N까지의 거리 저장
def BFS(N, M, grid, start):
    visited = [[False for _ in range(M)] for _ in range(N)]

    q = deque()
    q.append([start[0], start[1], 0])
    visited[start[0]][start[1]] = True
    result = [[start[0], start[1], 0]]  # start부터 다른 N까지의 거리 저장

    # 큐가 빌 때까지 반복
    while q:
        curY, curX, curDistance = q.popleft()

        for i in range(4):
            nextX = curX + pointX[i]
            nextY = curY + pointY[i]

            if 0 <= nextX < M and 0 <= nextY < N and visited[nextY][nextX] == False and grid[nextY][nextX] != '#':
                q.append([nextY, nextX, curDistance+1])
                visited[nextY][nextX] = True

                # N인 경우, 출발 지점으로부터 떨어진 거리를 저장
                if grid[nextY][nextX] != '.':
                    result.append([nextY, nextX, curDistance+1])

    return result


# city를 방문했는지 확인
def checkVisit(status, city):
    if status & (1 << city):
        return True
    return False


def TSP(N, graph, status, curV, DP, end):
    # 도시를 다 방문했고, end로의 경로가 존재한다면 here -> end 가는 값 반환
    if status == (1 << N) - 1:
        return graph[curV][end] if graph[curV][end] != -1 else INF

    # 이전에 계산한 값이면 그 값 반환
    if not DP[curV][status] == -1:
        return DP[curV][status]

    DP[curV][status] = INF

    # 방문하지 않은 도시들에 대해 반복
    for nextV in range(0, N):
        if not checkVisit(status, nextV) and not graph[curV][nextV] == -1:
            # (curV에서 nextV 가는 비용) + (nextV에서 나머지 도시를 거쳐 start로 가는 비용) 계산 및 nextV 방문처리
            temp = graph[curV][nextV] + TSP(N, graph, status | (1 << nextV), nextV, DP, end)

            # 최소값 갱신이 가능하다면 갱신
            if temp < DP[curV][status]:
                DP[curV][status] = temp
    
    return DP[curV][status]


def solve(N, M, K, grid):
    # 1. 시작 위치, 도착 위치, N 위치 파악
    start = None
    end = None
    food = dict()
    foodCount = 0

    for y in range(N):
        for x in range(M):
            if grid[y][x] == 'U':
                start = foodCount
            elif grid[y][x] == 'I':
                end = foodCount
            if grid[y][x] not in ['#', '.']:
                food[(y, x)] = foodCount
                food[foodCount] = (y, x)
                foodCount += 1

    # 2. 각 정점을 시작 정점으로 잡고 나머지 정점까지의 거리 도출 (시작, 도착 정점 포함)
    distance = [[-1 for _ in range(K+2)] for _ in range(K+2)]
    for cur in range(K+2):
        curDistance = BFS(N, M, grid, food[cur])
        for i in curDistance:
            tempY, tempX, tempDistance = i
            distance[cur][food[(tempY, tempX)]] = tempDistance
            distance[food[(tempY, tempX)]][cur] = tempDistance

    # 3. TSP 알고리즘으로 start에서 end까지의 최단거리 도출
    # end 정점은 가장 마지막에 방문해야 하므로, 미리 방문 표시 후 TSP 탐색 진행
    return TSP(K+2, distance, (1<<start) | (1<<end), start, [[-1 for _ in range(2**(K+2))] for _ in range((K+2))], end)


def main():
    N, M, K = map(int, input().split())
    grid = []
    for _ in range(N):
        grid.append(list(map(str, input().decode().strip())))

    print(solve(N, M, K, grid))


main()
