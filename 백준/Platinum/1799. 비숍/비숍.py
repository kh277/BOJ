# 백준 1799

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
result = [0, 0]


# 체스판에서 비숍이 놓인 칸의 개수 체크
def countGrid(N, grid, colorType):
    count = 0
    for i in range(N*N):
        if grid[i] == 2 and (i//N + i%N) % 2 == colorType:
            count += 1

    return count


# pos칸에 비숍을 놓을 수 있는지 여부 체크
def check(N, startP, grid):
    dx = [1, 1, -1, -1]
    dy = [1, -1, 1, -1]
    startX = startP%N
    startY = startP//N

    for i in range(4):
        curX = startX
        curY = startY

        while True:
            nextX = curX + dx[i]
            nextY = curY + dy[i]
            if 0 <= nextX < N and 0 <= nextY < N:
                if grid[nextY*N+nextX] == 2:
                    return False
            else:
                break
            curX = nextX
            curY = nextY

    return True


def backtrack(N, curP, grid, colorType):
    global result

    for nextP in range(curP, N*N):
        if grid[nextP] == 1 and (nextP//N + nextP%N) % 2 == colorType and check(N, nextP, grid) == True:
            # nextP에 비숍 배치 후 백트래킹
            grid[nextP] = 2
            backtrack(N, nextP, grid, colorType)

            # 배치 취소 후 다음 위치 탐색
            grid[nextP] = 1

    result[colorType] = max(result[colorType], countGrid(N, grid, colorType))


def solve(N, grid):
    # 흑/백을 분리하여 각각 백트래킹
    for color in range(2):
        for start in range(N*N):
            if grid[start] == 1 and (start//N + start%N) % 2 == color:
                backtrack(N, start, grid, color)


def main():
    N = int(input())
    grid = []
    for _ in range(N):
        grid.extend(list(map(int, input().split())))

    solve(N, grid)
    print(sum(result))


main()
