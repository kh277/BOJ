# 백준 2567

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 105
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def solve(N, square):
    grid = [[0 for _ in range(INF)] for _ in range(INF)]

    # 색종이가 붙은 부분 1로 변경
    for i in range(N):
        for y in range(square[i][1], square[i][1]+10):
            for x in range(square[i][0], square[i][0]+10):
                grid[y][x] = 1

    # 1로 표시된 칸 중 상하좌우에 0의 개수 총합 구하기
    circ = 0
    for curY in range(INF):
        for curX in range(INF):
            if grid[curY][curX] == 1:
                for i in range(4):
                    nextY = curY + dy[i]
                    nextX = curX + dx[i]
                    if grid[nextY][nextX] == 0:
                        circ += 1

    return circ


def main():
    N = int(input())
    square = []
    for _ in range(N):
        square.append(list(map(int, input().split())))
    print(solve(N, square))


main()
