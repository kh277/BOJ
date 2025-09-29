# 백준 34444

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(grid):
    for i in range(9):
        setY = set()
        setX = set()
        for j in range(9):
            setY.add(grid[i][j])
            setX.add(grid[j][i])
        if len(setY) != 9 or len(setX) != 9:
            return "INVALID!"

    for y in range(0, 9, 3):
        for x in range(0, 9, 3):
            setA = set()
            for dy in [0, 1, 2]:
                for dx in  [0, 1, 2]:
                    setA.add(grid[y+dy][x+dx])
            if len(setA) != 9:
                return "INVALID!"

    return "VALID"


def main():
    grid = []
    for _ in range(9):
        grid.append(list(map(int, input().split())))
    print(solve(grid))


main()
