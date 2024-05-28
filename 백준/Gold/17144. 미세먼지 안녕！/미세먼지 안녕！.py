# 백준 17144

import sys
from copy import deepcopy

input = sys.stdin.readline


# 공기청정기의 y좌표 리턴
def find_air_cleaner(R: int, T: int, graph: list) -> int:
    for y in range(R):
            for x in range(T):
                if graph[y][x] == -1:
                    return y


# 모든 미세먼지 값의 총합 리턴
def check_fine_dust(R: int, T: int, graph: list) -> int:
    fine_dust = 0

    for y in range(R):
        for x in range(T):
            if graph[y][x] == -1:
                continue
            else:
                fine_dust += graph[y][x]
    
    return fine_dust


def solve(R: int, T: int, C: int, graph: list) -> int:
    # (y좌표, x좌표) 순서로 저장
    point = [(1, 0), (-1, 0), (0, -1), (0, 1)]

    count = 1

    # 공기청정기의 위치 확인
    upper = find_air_cleaner(R, T, graph)
    lower = upper+1

    while True:
        # 1. 미세먼지 확산
        temp = deepcopy(graph)
        for y in range(R):
            for x in range(T):
                # 해당 칸에 미세먼지가 존재할 경우
                if graph[y][x] not in [0, -1]:
                    cur = graph[y][x]
                    
                    for i in range(4):
                        nextY = y + point[i][0]
                        nextX = x + point[i][1]
                        # 근처 좌표가 벽과 공기청정기가 아닐 경우
                        if 0 <= nextY < R and 0 <= nextX < T and graph[nextY][nextX] != -1:
                            temp[nextY][nextX] += cur // 5
                            temp[y][x] -= cur // 5
        graph = temp
                            
        # 2-1. 위쪽 공기청정기 작동
        for y in range(upper-1, 0, -1):
            graph[y][0] = graph[y-1][0]
        for x in range(1, T):
            graph[0][x-1] = graph[0][x]
        for y in range(1, upper+1):
            graph[y-1][T-1] = graph[y][T-1]
        for x in range(T-1, 1, -1):
            graph[upper][x] = graph[upper][x-1]
        graph[upper][1] = 0 
        
        # 2-2. 아래쪽 공기청정기 작동
        for y in range(lower+1, R-1):
            graph[y][0] = graph[y+1][0]
        for x in range(1, T):
            graph[R-1][x-1] = graph[R-1][x]
        for y in range(R-1, lower, -1):
            graph[y][T-1] = graph[y-1][T-1]
        for x in range(T-1, 1, -1):
            graph[lower][x] = graph[lower][x-1]
        graph[lower][1] = 0

        # #. 종료조건
        if count == C:
            return check_fine_dust(R, T, graph)

        count += 1


def main():
    R, T, C = map(int, input().split())

    graph = []
    for _ in range(R):
        graph.append(list(map(int, input().split())))
    
    print(solve(R, T, C, graph))


main()