# 백준 17353

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


# num이상의 2의 제곱수 반환
def square(num):
    result = 1
    while True:
        if result >= num:
            return result
        result *= 2


# 0-base, 구간 [left, right]에 +value를 처리하는 쿼리
def imosUpdate(N, tree, left, right, value):
    # 왼쪽 구간 처리
    left += N
    tree[left] += value
    while left > 1:
        left >>= 1
        tree[left] = tree[left<<1] + tree[left<<1 | 1]

    # 오른쪽 구간 처리
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
    size = square(N+1)
    num = list(map(int, input().split()))

    sumTree = array('i', [0]) * (size*2)
    leftTree = array('i', [0]) * (size*2)

    Q = int(input())
    for _ in range(Q):
        q = list(map(int, input().split()))
        if q[0] == 1:
            l = q[1]
            r = q[2]
            imosUpdate(size, sumTree, l-1, r-1, 1)
            imosUpdate(size, leftTree, l-1, r-1, l)
        else:
            x = q[1]
            print(num[x-1] + imosQuery(size, sumTree, x-1) * (x+1) - imosQuery(size, leftTree, x-1))


main()
