# 백준 14053


import sys

input = sys.stdin.readline


def clean_check_all(N: int, M: int, graph: list) -> int:
    for y in range(N):
        for x in range(M):
            if graph[y][x] == 0:
                return False
    
    return True


def clean_check_4point(N: int, M: int, graph: list, cur: list) -> int:
    pointX = [0, 1, 0, -1]
    pointY = [-1, 0, 1, 0]

    for i in range(4):
        nextY = cur[0] + pointY[i]
        nextX = cur[1] + pointX[i]
        
        # 청소되지 않은 칸이 있는지 확인
        if graph[nextY][nextX] == 0:
            return False

    return True


def solve(N: int, M: int, graph: list, start: list) -> int:
    pointX = [0, 1, 0, -1]
    pointY = [-1, 0, 1, 0]

    count = 0
    
    # [현재 y좌표, 현재 x좌표, 바라보는 방향] 순으로 저장
    cur = start

    while True:
        # 1. 현재 칸이 아직 청소되지 않은 경우 -> 청소
        if graph[cur[0]][cur[1]] == 0:
            graph[cur[0]][cur[1]] = -1
            count += 1
        
        # 2. 현재 칸의 주변 4칸이 전부 깨끗한 경우
        if clean_check_4point(N, M, graph, cur):
            for i in range(4):
                # 각 방향별로 뒤쪽에 벽이 있는 경우
                if cur[2] == i and graph[cur[0]-pointY[i]][cur[1]-pointX[i]] == 1:
                    return count
                # 벽이 없는 경우
                elif cur[2] == i:
                    cur[0] = cur[0] - pointY[i]
                    cur[1] = cur[1] - pointX[i]
                    break

        # 3. 현재 칸의 주변 4칸 중 청소할 곳이 있는 경우
        else:
            # 90도 회전 및 방향 확인
            for i in range(cur[2]+3, cur[2]+13, 3):
                i = i % 4
                cur[2] = i

                # 앞쪽에 청소할 칸이 있는 경우 한 칸 전진
                if graph[cur[0]+pointY[i]][cur[1]+pointX[i]] == 0:
                    cur[0] = cur[0] + pointY[i]
                    cur[1] = cur[1] + pointX[i]
                    break


def main():
    N, M = map(int, input().split())

    r, c, d = map(int, input().split())

    graph = []
    for i in range(N):
        graph.append(list(map(int, input().split())))

    print(solve(N, M, graph, [r, c, d]))


main()