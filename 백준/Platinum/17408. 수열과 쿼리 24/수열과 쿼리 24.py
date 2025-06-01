# 백준 17408

'''
세그먼트 트리 2개로 구간 내의 제일 큰 값, 구간 내의 두 번째로 큰 값을 저장한다.
'''

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
ARRAY_TYPE = 'I'


# num이상의 2의 제곱수 반환
def square(num):
    result = 1
    while True:
        if result >= num:
            return result
        result *= 2


# 크기가 N인 세그먼트 트리 빌드
def build(N, A):
    tree1 = array(ARRAY_TYPE, [0]) * (N*2)
    tree2 = array(ARRAY_TYPE, [0]) * (N*2)

    for index in range(len(A)):
        tree1[N+index] = A[index]

    for index in range(N-1, 0, -1):
        if tree1[index<<1] > tree1[index<<1 | 1]:
            tree1[index] = tree1[index<<1]
            tree2[index] = max(tree2[index<<1], tree1[index<<1 | 1])
        else:
            tree1[index] = tree1[index<<1 | 1]
            tree2[index] = max(tree1[index<<1], tree2[index<<1 | 1])
    return tree1, tree2


# index번째 값을 value로 변경
def update(N, tree1, tree2, index, value):
    index += N
    tree1[index] = value

    while index > 1:
        index >>= 1
        if tree1[index<<1] > tree1[index<<1 | 1]:
            tree1[index] = tree1[index<<1]
            tree2[index] = max(tree2[index<<1], tree1[index<<1 | 1])
        else:
            tree1[index] = tree1[index<<1 | 1]
            tree2[index] = max(tree1[index<<1], tree2[index<<1 | 1])


# 0-base, 구간 [left, right]에서 제일 큰 값과 두 번째로 큰 값을 더한 값 반환
def query(N, tree1, tree2, left, right):
    result1 = 0
    result2 = 0
    left += N
    right += N

    while left <= right:
        if left & 1:
            if tree1[left] > result1:
                result2 = max(result1, tree2[left])
                result1 = tree1[left]
            else:
                result2 = max(result2, tree1[left])
            left += 1
        if ~right & 1:
            if tree1[right] > result1:
                result2 = max(result1, tree2[right])
                result1 = tree1[right]
            else:
                result2 = max(result2, tree1[right])
            right -= 1
        left >>= 1
        right >>= 1

    return result1 + result2


def main():
    N = int(input())
    size = square(N)
    tree1, tree2 = build(size, list(map(int, input().split())))

    M = int(input())
    for _ in range(M):
        a, b, c = map(int, input().split())
        if a == 1:
            update(size, tree1, tree2, b-1, c)
        else:
            print(query(size, tree1, tree2, b-1, c-1))


main()
