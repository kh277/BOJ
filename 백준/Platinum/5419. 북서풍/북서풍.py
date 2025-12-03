# 백준 5419

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


# index번째 인덱스의 값을 value만큼 추가
def update(N, tree, index, value):
    index += N
    tree[index] += value

    while index > 1:
        index >>= 1
        tree[index] = tree[index<<1] + tree[index<<1 | 1]


# left ~ right까지의 합 계산
def query(N, tree, left, right):
    result = 0
    left += N
    right += N

    while left <= right:
        if left & 1:
            result += tree[left]
            left += 1
        if ~right & 1:
            result += tree[right]
            right -= 1
            
        left >>= 1
        right >>= 1

    return result


# value 좌표에 대해 압축
def compress(N, point, value):
    point.sort(key= lambda x: x[value])
    before = point[0][value]
    compress = 0
    for i in range(N):
        if point[i][value] == before:
            point[i][value] = compress
        else:
            before = point[i][value]
            compress += 1
            point[i][value] = compress

    return point


def solve(N, point):
    # 좌표 압축 및 정렬
    point = compress(N, point, 0)
    point = compress(N, point, 1)
    point.sort(key= lambda x: (x[1], -x[0]))

    tree = array('I', [0]) * (N*2)

    # y좌표가 작은 점들부터 세그먼트 트리에 추가 및 쿼리 처리
    total = 0
    for i in range(N):
        update(N, tree, point[i][0], 1)
        total += query(N, tree, point[i][0], N-1) - 1

    return total


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        point = []
        for _ in range(N):
            point.append(list(map(int, input().split())))

        print(solve(N, point))


main()
