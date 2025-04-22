# 백준 3042

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


# A, B, C가 한 직선 위에 있는지 체크
def checkLine(A, B, C):
    dx1 = B[1]-A[1]
    dy1 = B[0]-A[0]
    dx2 = C[1]-A[1]
    dy2 = C[0]-A[0]

    if dx1 == 0 or dx2 == 0:
        if dx1 == dx2:
            return True
        return False

    return True if dy1/dx1 == dy2/dx2 else False


def solve(N, grid):
    data = []
    for y in range(N):
        for x in range(N):
            if grid[y][x] != '.':
                data.append([y, x])

    count = 0
    for a in range(len(data)-2):
        for b in range(a+1, len(data)-1):
            for c in range(b+1, len(data)):
                if checkLine(data[a], data[b], data[c]) == True:
                    count += 1

    return count


def main():
    N = int(input())
    grid = []
    for _ in range(N):
        grid.append(list(input().decode().strip()))

    print(solve(N, grid))


main()