# 백준 16975

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
ARRAY_TYPE = 'l'


# num이상의 2의 제곱수 반환
def square(num):
    result = 1
    while True:
        if result >= num:
            return result
        result *= 2


# 크기가 N인 세그먼트 트리 빌드
def build(N, A):
    tree = array(ARRAY_TYPE, [0]) * (N*2)
    for i in range(len(A)):
        tree[N+i] = A[i]

    while index > 1:
        index >>= 1
        tree[index] = tree[index<<1] + tree[index<<1 | 1]

    return tree


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
    size = square(N)
    num = list(map(int, input().split()))
    tree = array(ARRAY_TYPE, [0]) * (size*2)

    Q = int(input())
    for _ in range(Q):
        q = list(map(int, input().split()))
        if q[0] == 1:
            _, i, j, k = q
            imosUpdate(size, tree, i-1, j-1, k)
        else:
            x = q[1]
            print(num[x-1] + imosQuery(size, tree, x-1))


main()
