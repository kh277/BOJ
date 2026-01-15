# 백준 2782

'''
DP[status][curV] = 방문 상태가 status이고 현재 curV에 있을 때, 걸린 최소 시간
'''

import io
from collections import deque
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
INF = 10**9


# 왕, 왕비, 나무의 위치 저장
def getPos(Y, X, grid, tree, dictV):
    kingV = None
    queenV = None

    for y in range(Y):
        for x in range(X):
            curP = y*X + x
            if grid[y][x] == ord('K'):
                kingV = curP
            elif grid[y][x] == ord('Q'):
                queenV = curP
            elif grid[y][x] == ord('G'):
                dictV[curP] = len(tree)
                tree.append(curP)

    # 왕과 왕비를 맨 마지막에 추가
    dictV[kingV] = len(tree)
    tree.append(kingV)
    dictV[queenV] = len(tree)
    tree.append(queenV)


# 격자에서 각 정점 별 거리 도출
def BFS(Y, X, grid, graph, dictV, startV, startI):
    N = Y * X
    q = deque()
    dist = array('i', [INF]) * N
    q.append(startI)
    dist[startI] = 0

    while q:
        curP = q.popleft()
        curDist = dist[curP]
        curY, curX = divmod(curP, X)

        # 왕, 왕비, 나무 중 하나일 경우
        v = dictV.get(curP)
        if v != None:
            graph[startV][v] = curDist

        # 다음 정점 탐색
        for i in range(4):
            nextX = curX + dx[i]
            nextY = curY + dy[i]
            if 0 <= nextX < X and 0 <= nextY < Y:
                nextP = nextY*X + nextX
                if dist[nextP] == INF and grid[nextY][nextX] != ord('#'):
                    q.append(nextP)
                    dist[nextP] = curDist+1


def getMaxCount(V, T, graph):
    startV = V-2
    endV = V-1
    N = V-2
    maxCount = 0
    DP = [array('i', [INF]) * N for _ in range(1<<N)]

    for nextV in range(N):
        curT = graph[startV][nextV]
        if curT < INF:
            DP[1<<nextV][nextV] = curT

    for curS in range(1<<N):
        count = curS.bit_count()
        for curV in range(N):
            # 방문하지 않은 정점이거나 도달할 수 없는 정점인 경우
            if curS & (1<<curV) == 0 or DP[curS][curV] >= INF:
                continue

            # 현재 정점에서 도착 정점으로 가는 경우
            if graph[curV][endV] < INF and DP[curS][curV] + (count+1)*graph[curV][endV] <= T and count > maxCount:
                maxCount = count

            # 다음 정점으로 이동하는 경우
            for nextV in range(N):
                if curS & (1<<nextV) != 0 or graph[curV][nextV] >= INF:
                    continue
                nextS = curS | (1<<nextV)
                nextT = DP[curS][curV] + (count+1)*graph[curV][nextV]
                if nextT <= T and DP[nextS][nextV] > nextT:
                    DP[nextS][nextV] = nextT

    return maxCount


def solve(Y, X, T, grid):
    # 왕, 왕비, 나무 좌표 저장
    tree = []
    dictV = dict()
    getPos(Y, X, grid, tree, dictV)

    # BFS로 각 정점 별 거리 도출
    V = len(tree)
    graph = [[INF] * V for _ in range(V)]
    for i in range(V):
        BFS(Y, X, grid, graph, dictV, i, tree[i])

    # DP로 최대 선물 개수 구하기
    return getMaxCount(V, T, graph)


def main():
    T = int(input())
    for _ in range(T):
        Y, X, T = map(int, input().split())
        grid = []
        for _ in range(Y):
            grid.append(list(input().strip()))
        print(solve(Y, X, T, grid))


main()
