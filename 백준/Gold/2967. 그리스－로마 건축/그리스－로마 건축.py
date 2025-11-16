# 백준 2967

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


# 시작점 역전 여부는 rev에 따라, moveType 방향대로 탐색했을 때 가장 처음 만나는 직사각형의 정보 반환
def find(Y, X, grid, rev, moveType):
    size = 0
    if rev == 0:
        # (0, 0)에서 왼쪽으로
        if moveType == 0:
            for y in range(Y):
                for x in range(X):
                    if grid[y][x] == 'x':
                        for _ in range(min(X-x, Y-y)):
                            if grid[y+size][x] == '.' or grid[y][x+size] == '.':
                                break
                            size += 1
                        return (y, x, size)

        # (0, 0)에서 아래쪽으로
        else:
            for x in range(X):
                for y in range(Y):
                    if grid[y][x] == 'x':
                        for _ in range(min(X-x, Y-y)):
                            if grid[y+size][x] == '.' or grid[y][x+size] == '.':
                                break
                            size += 1
                        return (y, x, size)

    else:
        # (Y-1, X-1)에서 오른쪽으로
        if moveType == 0:
            for y in range(Y-1, -1, -1):
                for x in range(X-1, -1, -1):
                    if grid[y][x] == 'x':
                        for _ in range(min(x+1, y+1)):
                            if grid[y-size][x] == '.' or grid[y][x-size] == '.':
                                break
                            size += 1
                        return (y-size+1, x-size+1, size)

        # (Y-1, X-1)에서 위쪽으로
        else:
            for x in range(X-1, -1, -1):
                for y in range(Y-1, -1, -1):
                    if grid[y][x] == 'x':
                        for _ in range(min(x+1, y+1)):
                            if grid[y-size][x] == '.' or grid[y][x-size] == '.':
                                break
                            size += 1
                        return (y-size+1, x-size+1, size)


def solve(Y, X, grid):
    result = set()

    for i in range(2):
        for j in range(2):
            a, b, r = find(Y, X, grid, i, j)
            result.add((a+1, b+1, r))

    if len(result) == 1:
        return list(result) * 2
    return list(result)


def main():
    Y, X = map(int, input().split())
    grid = []
    for _ in range(Y):
        grid.append(list(input().decode().strip()))
    
    for i in solve(Y, X, grid):
        print(*i)


main()
