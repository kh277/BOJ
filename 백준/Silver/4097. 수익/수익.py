# 백준 4097

'''
세그먼트 트리의 각 노드에는 [구간의 왼쪽 접두사 포함 최대 연속합,
구간의 오른쪽 접미사 포함 최대 연속합, 구간 내 최대 연속합, 구간 내 총합] 저장.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**10


def square(num):
    result = 1
    while True:
        if result >= num:
            return result
        result *= 2


# left노드 + right노드에서 최대 연속합 노드 처리 
def combine(leftN, rightN):
    return [max(leftN[0], leftN[3]+rightN[0]),
            max(rightN[1], leftN[1]+rightN[3]),
            max(leftN[2], rightN[2], leftN[1]+rightN[0]),
            leftN[3] + rightN[3]]


# 세그먼트 트리 빌드
def build(N, A):
    tree = [[0, 0, 0, 0] for _ in range(N*2)]
    for i in range(len(A)):
        for j in range(4):
            tree[N+i][j] = A[i]

    for i in range(N-1, 0, -1):
        left = i<<1
        right = i<<1 | 1

        tree[i] = combine(tree[left], tree[right])

    return tree


# 구간 [left, right]에서 가장 큰 연속합 출력
def query(N, tree, left, right):
    resultL = [-INF, -INF, -INF, 0]
    resultR = [-INF, -INF, -INF, 0]
    left += N
    right += N

    while left <= right:
        if left & 1:
            resultL = combine(resultL, tree[left])
            left += 1
        if ~right & 1:
            resultR = combine(tree[right], resultR)
            right -= 1

        left >>= 1
        right >>= 1

    return combine(resultL, resultR)[2]


def main():
    while True:
        N = int(input())
        if N == 0:
            break
        treeSize = square(N)
        A = []
        for _ in range(N):
            A.append(int(input()))

        # 세그먼트 트리 
        tree = build(treeSize, A)

        # 쿼리 처리
        print(query(treeSize, tree, 0, N-1))


main()
