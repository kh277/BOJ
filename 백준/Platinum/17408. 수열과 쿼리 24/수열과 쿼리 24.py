# 백준 17408

'''
세그먼트 트리의 각 노드는 [구간 내의 제일 큰 값, 구간 내의 두 번째로 큰 값]을 저장한다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


# num이상의 2의 제곱수 반환
def square(num):
    result = 1
    while True:
        if result >= num:
            return result
        result *= 2


# 크기가 N인 세그먼트 트리 빌드
def build(N, A):
    tree = [[0, 0] for _ in range(N*2)]
    for i in range(len(A)):
        tree[N+i] = [A[i], 0]

    for i in range(N-1, 0, -1):
        if tree[i<<1][0] > tree[i<<1 | 1][0]:
            tree[i] = [tree[i<<1][0], max(tree[i<<1][1], tree[i<<1 | 1][0])]
        else:
            tree[i] = [tree[i<<1 | 1][0], max(tree[i<<1][0], tree[i<<1 | 1][1])]

    return tree


# index번째 값을 value로 변경
def update(N, tree, index, value):
    index += N
    tree[index] = [value, 0]

    while index > 1:
        index >>= 1
        if tree[index<<1][0] > tree[index<<1 | 1][0]:
            tree[index] = [tree[index<<1][0], max(tree[index<<1][1], tree[index<<1 | 1][0])]
        else:
            tree[index] = [tree[index<<1 | 1][0], max(tree[index<<1][0], tree[index<<1 | 1][1])]


# 0-base, 구간 [left, right]에서 제일 큰 값과 두 번째로 큰 값을 더한 값 반환
def query(N, tree, left, right):
    result1 = 0
    result2 = 0
    left += N
    right += N

    while left <= right:
        if left & 1:
            if tree[left][0] > result1:
                result2 = max(result1, tree[left][1])
                result1 = tree[left][0]
            else:
                result2 = max(result2, tree[left][0])
            left += 1
        if ~right & 1:
            if tree[right][0] > result1:
                result2 = max(result1, tree[right][1])
                result1 = tree[right][0]
            else:
                result2 = max(result2, tree[right][0])
            right -= 1
        left >>= 1
        right >>= 1

    return result1 + result2


def main():
    N = int(input())
    size = square(N)
    tree = build(size, list(map(int, input().split())))

    M = int(input())
    for _ in range(M):
        a, b, c = map(int, input().split())
        if a == 1:
            update(size, tree, b-1, c)
        else:
            print(query(size, tree, b-1, c-1))


main()
