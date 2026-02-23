# 백준 11658

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


# Y*X 크기의 arr을 기반으로 2D Fenwick Tree 생성
def build(Y, X, arr):
    tree = [[0] * (X+1) for _ in range(Y+1)]

    for y in range(1, Y+1):
        for x in range(1, X+1):
            tree[y][x] = arr[y-1][x-1]
    for y in range(1, Y+1):
        for x in range(1, X+1):
            nextX = x + (x & -x)
            if nextX <= X:
                tree[y][nextX] += tree[y][x]
    for y in range(1, Y+1):
        nextY = y + (y & -y)
        if nextY <= Y:
            for x in range(1, X+1):
                tree[nextY][x] += tree[y][x]

    return tree


# Y*X 크기의 tree에서 [tY][tX] 위치의 값에 diff 더하기
def update(Y, X, tree, tY, tX, diff):
    y = tY
    while y <= Y:
        x = tX
        while x <= X:
            tree[y][x] += diff
            x += (x & -x)
        y += (y & -y)


# y범위 [0, tY], x범위 [0, tX]에 대해 구간 합 쿼리
def basicQuery(tree, tY, tX):
    result = 0
    y = tY
    while y > 0:
        x = tX
        while x > 0:
            result += tree[y][x]
            x -= (x & -x)
        y -= (y & -y)

    return result


# y범위 [sY, eY], x범위 [sX, eX]에 대해 구간 합 쿼리
def query(tree, sY, sX, eY, eX):
    return (basicQuery(tree, eY, eX)
        - basicQuery(tree, eY, sX-1)
        - basicQuery(tree, sY-1, eX)
        + basicQuery(tree, sY-1, sX-1))


def main():
    N, M = map(int, input().split())
    grid = []
    for _ in range(N):
        grid.append(list(map(int, input().split())))

    # 펜윅 트리 생성
    tree = build(N, N, grid)

    # 쿼리 처리
    for _ in range(M):
        w, *q = map(int, input().split())
        if w == 0:
            y, x, v = q[0], q[1], q[2]
            update(N, N, tree, y, x, v-grid[y-1][x-1])
            grid[y-1][x-1] = v
        else:
            sY, sX, eY, eX = q[0], q[1], q[2], q[3]
            print(query(tree, sY, sX, eY, eX))


main()
