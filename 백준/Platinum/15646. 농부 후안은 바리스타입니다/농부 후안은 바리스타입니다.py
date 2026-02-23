# 백준 15646

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


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


def main():
    X, Y, Q = map(int, input().split())

    # 펜윅 트리 생성
    tree = [[0] * (X+1) for _ in range(Y+1)]

    # 차분 배열을 이용해 쿼리 처리
    for _ in range(Q):
        w, *q = map(int, input().split())
        if w == 1:
            x1, y1, x2, y2, d = q
            update(Y, X, tree, y1, x1, d)
            if x2 < X:
                update(Y, X, tree, y1, x2+1, -d)
            if y2 < Y:
                update(Y, X, tree, y2+1, x1, -d)
            if x2 < X and y2 < Y:
                update(Y, X, tree, y2+1, x2+1, d)
        else:
            x, y = q
            print(basicQuery(tree, y, x))


main()
