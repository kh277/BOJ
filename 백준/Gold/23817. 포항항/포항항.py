# 백준 23817

'''
1~20개의 식당 중 5개의 식당을 방문하는 최소 시간을 구해야 한다.

1. 그래프에서 시작 위치와 식당의 위치를 파악한다.
2. 시작 위치를 포함하여 각 식당끼리 거리를 간선으로 작성한다.
3. 시작 위치에서 식당 5개를 지나는 데 걸리는 최소시간을 구한다.
'''

import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline


# start에서 다른 모든 정점까지의 거리 저장
def BFS(graph: list, start: list) -> list:
    N = len(graph)      # 세로 길이
    M = len(graph[0])   # 가로 길이

    pointX = [-1, 1, 0, 0]
    pointY = [0, 0, -1, 1]

    q = deque()
    q.append([start[0], start[1], 0])
    graph[start[0]][start[1]] = 'X'

    result = [[start[0], start[1], 0]]  # 식당까지의 거리 저장

    # 큐가 빌 때까지 반복
    while q:
        temp = q.popleft()

        

        # 상하좌우 탐색 가능한지 확인
        for i in range(4):
            nextY = temp[0] + pointY[i]
            nextX = temp[1] + pointX[i]

            # 탐색 가능한 경우 큐에 넣고 정점까지의 거리를 graph에 표시
            if 0 <= nextX < M and 0 <= nextY < N and graph[nextY][nextX] != 'X':
                q.append([nextY, nextX, temp[2]+1])

                # 다음 탐색 지점이 식당이라면 결과 리스트에 저장
                if graph[nextY][nextX] == 'K':
                    result.append([nextY, nextX, temp[2]+1])

                graph[nextY][nextX] = 'X'

    return result


# num으로 입력된 숫자 중 중복이 있는지 확인
def duplicate_check(num: list) -> bool:
    temp = set(num)
    if len(temp) == len(num):
        return True
    
    return False


def solve(N: int, M: int, graph: list) -> int:
    start = []
    cafe = []

    # 1. 시작위치와 식당의 위치(cafe) 파악
    for y in range(N):
        for x in range(M):
            if graph[y][x] == 'S':
                start = [y, x]
            elif graph[y][x] == 'K':
                cafe.append([y, x])

    # cafe 리스트의 0번 정점은 시작지점을 나타냄
    cafe = [start] + cafe

    # 2. 한 식당에서 다른 식당까지의 거리(length) 파악
    length = [[-1 for _ in  range(len(cafe))] for _ in range(len(cafe))]

    # cafe[i] 정점을 시작 지점으로 하여 거리 정보 반환
    for i in range(len(cafe)):
        cafe_length = BFS(deepcopy(graph), cafe[i])
        for j in cafe_length:
            for k in range(len(cafe)):
                # 좌표가 일치한다면, cafe[i]에서 cafe[k]로 가는 비용은 j[2]
                if j[0] == cafe[k][0] and j[1] == cafe[k][1]:
                    length[i][k] = j[2]
    
    
    # 3. 시작 지점에서 식당 5개를 지나는 데 걸리는 시간 구하기
    result = 10e5
    for a in range(1, len(cafe)):
        if length[0][a] == -1:
            continue
        for b in range(1, len(cafe)):
            if a == b or length[a][b] == -1:
                continue
            for c in range(1, len(cafe)):
                if a == c or b == c or length[b][c] == -1:
                    continue
                for d in range(1, len(cafe)):
                    if a == d or b == d or c == d or length[c][d] == -1:
                        continue
                    for e in range(1, len(cafe)):
                        if a == e or b == e or c == e or d == e or length[d][e] == -1:
                            continue
                        result = min(result, length[0][a] + length[a][b] + length[b][c] + length[c][d] + length[d][e])

    # 5개의 식당을 방문할 수 없는 경우
    if result == 10e5:
        return -1

    return result


def main():
    N, M = map(int, input().split())

    graph = []
    for y in range(N):
        graph.append(list(input().rstrip()))

    print(solve(N, M, graph))


main()
