# 백준 18246

'''
먼저, N개의 색종이 추가 쿼리를 차분 배열에 저장해 준다.
색종이 제거 쿼리가 들어오지 않으므로, 차분 배열을 풀어 각 좌표별로 중첩된 색종이의 수를 배열에 저장해준다.
이 배열을 기반으로 2D 세그먼트 트리를 작성하고, 구간 최대값 쿼리를 처리해 주면 된다.
'''

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
MAX = 1510


# Y*X 크기의 arr을 기반으로 2D Segment Tree 생성
def build(Y, X, arr):
    tree = [array('i', [0]) * (X<<1) for _ in range(Y<<1)]

    for y in range(len(arr)):
        for x in range(len(arr[0])):
            tree[Y + y][X + x] = arr[y][x]
    for y in range(Y, Y<<1):
        for x in range(X-1, 0, -1):
            tree[y][x] = max(tree[y][x<<1], tree[y][x<<1 | 1])
    for y in range(Y-1, 0, -1):
        for x in range(1, X<<1):
            tree[y][x] = max(tree[y<<1][x], tree[y<<1 | 1][x])

    return tree


# tree[curY] 에서 x범위 [sX, eX]에 대해 구간 합 쿼리
def queryX(X, tree, curY, sX, eX):
    result = 0
    x1 = sX + X
    x2 = eX + X

    while x1 <= x2:
        if x1 & 1:
            result = max(result, tree[curY][x1])
            x1 += 1
        if ~x2 & 1:
            result = max(result, tree[curY][x2])
            x2 -= 1
        x1 >>= 1
        x2 >>= 1

    return result


# y범위 [sY, eY], x범위 [sX, eX]에 대해 구간 합 쿼리
def query(Y, X, tree, sY, sX, eY, eX):
    result = 0
    y1 = sY + Y
    y2 = eY + Y

    while y1 <= y2:
        if y1 & 1:
            result = max(result, queryX(X, tree, y1, sX, eX))
            y1 += 1
        if ~y2 & 1:
            result = max(result, queryX(X, tree, y2, sX, eX))
            y2 -= 1
        y1 >>= 1
        y2 >>= 1

    return result


def main():
    N, Q = map(int, input().split())

    # 차분 배열 생성
    diff = [array('i', [0]) * MAX for _ in range(MAX)]

    # 차분 배열에 색종이 추가
    for _ in range(N):
        y1, x1, y2, x2 = map(int, input().split())
        diff[y1][x1] += 1
        diff[y2][x1] -= 1
        diff[y1][x2] -= 1
        diff[y2][x2] += 1

    # 차분 배열 해체
    for y in range(MAX):
        for x in range(1, MAX):
            diff[y][x] += diff[y][x-1]
    for x in range(MAX):
        for y in range(1, MAX):
            diff[y][x] += diff[y-1][x]

    # 2차원 세그먼트 트리 생성
    size = MAX
    tree = build(size, size, diff)

    # 쿼리 처리
    for _ in range(Q):
        y1, x1, y2, x2 = map(int, input().split())
        print(query(size, size, tree, y1, x1, y2-1, x2-1))


main()
