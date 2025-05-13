# 백준 18436

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def square(num):
    result = 1
    while True:
        if result >= num:
            return result
        result *= 2


# 세그먼트 트리 빌드
def build(N, A):
    tree = [[0, 0] for _ in range(N*2)]
    for i in range(len(A)):
        tree[N+i][A[i]%2] += 1

    for i in range(N-1, 0, -1):
        left = i<<1
        right = i<<1 | 1
        tree[i][0] = tree[left][0] + tree[right][0]
        tree[i][1] = tree[left][1] + tree[right][1]

    return tree


# index번째 인덱스를 value로 변경
def update(N, tree, index, value):
    index += N
    tree[index][value%2] = 1
    tree[index][(value+1)%2] = 0
    
    while index > 1:
        index >>= 1
        tree[index] = [tree[index<<1][0] + tree[index<<1 | 1][0], tree[index<<1][1] + tree[index<<1 | 1][1]]


# 구간 [left, right]에서 짝수, 홀수의 개수 반환
def query(N, tree, left, right, numType):
    result = 0
    left += N
    right += N

    while left <= right:
        if left & 1:
            result += tree[left][numType%2]
            left += 1
        if ~right & 1:
            result += tree[right][numType%2]
            right -= 1

        left >>= 1
        right >>= 1

    return result


def main():
    N = int(input())
    treeSize = square(N)
    A = list(map(int, input().split()))
    tree = build(treeSize, A)

    M = int(input())
    for _ in range(M):
        t, a, b = map(int, input().split())
        if t == 1:
            update(treeSize, tree, a-1, b)
        elif t == 2:
            print(query(treeSize, tree, a-1, b-1, 0))
        else:
            print(query(treeSize, tree, a-1, b-1, 1))


main()
