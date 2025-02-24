# 백준 16993

'''
각 노드는 [구간의 왼쪽 접두사 포함 최대 연속합, 구간의 오른쪽 접미사 포함 최대 연속합,
    구간 내 최대 연속합, 구간 내 총합] 저장.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**9


def square(num):
    result = 1
    while True:
        if result >= num:
            return result
        result *= 2


# left노드 + right노드에서 최대 연속합 노드 처리 
def combine(leftNode, rightNode):
    return [max(leftNode[0], leftNode[3]+rightNode[0]),
            max(rightNode[1], leftNode[1]+rightNode[3]),
            max(leftNode[2], rightNode[2], leftNode[1]+rightNode[0]),
            leftNode[3] + rightNode[3]]


# 세그먼트 트리 구성
def init(N, tree):
    for i in range(N-1, 0, -1):
        left = i<<1
        right = i<<1 | 1

        tree[i] = combine(tree[left], tree[right])


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
    tempN = int(input())
    N = square(tempN)
    A = list(map(int, input().split()))

    # 세그먼트 트리 기본 설정
    tree = [[0, 0, 0, 0] for _ in range(N*2)]
    for i in range(tempN):
        tree[N+i] = [A[i], A[i], A[i], A[i]]
    init(N, tree)

    # 쿼리 처리
    M = int(input())
    for _ in range(M):
        s, e = map(int, input().split())
        print(query(N, tree, s-1, e-1))


main()
