# 백준 2934

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
ARRAY_TYPE = 'i'


def square(num):
    result = 1
    while True:
        if result >= num:
            return result
        result <<= 1


# 0-base, 구간 [left, right]에 +value를 처리하는 쿼리
def imosUpdate(N, tree, left, right, value):
    left += N
    tree[left] += value
    while left > 1:
        left >>= 1
        tree[left] = tree[left<<1] + tree[left<<1 | 1]

    right += 1
    if right < N:
        right += N
        tree[right] -= value
        while right > 1:
            right >>= 1
            tree[right] = tree[right<<1] + tree[right<<1 | 1]


# tree[index]의 값을 구하는 쿼리
def imosQuery(N, tree, index):
    result = 0
    left = N
    right = N + index

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


def main():
    N = int(input())
    size = square(100001)
    tree = array(ARRAY_TYPE, [0]) * (size*2)
    used = array(ARRAY_TYPE, [0]) * size

    for _ in range(N):
        a, b = map(int, input().split())
        # 쿼리 처리
        startFlower = imosQuery(size, tree, a)
        endFlower = imosQuery(size, tree, b)
        print(startFlower - used[a] + endFlower - used[b])
        used[a] = startFlower
        used[b] = endFlower

        # 업데이트 처리
        imosUpdate(size, tree, a+1, b-1, 1)


main()
