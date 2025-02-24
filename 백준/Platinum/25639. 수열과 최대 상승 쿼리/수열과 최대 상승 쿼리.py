# 백준 16993

'''
각 노드는 [구간 내 최대 상승 값, 구간 내 최대값, 구간 내 최소값] 저장.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


# left구간 + right구간에서 최대 상승 값 처리 
def combine(leftNode, rightNode):
    return [max(leftNode[0], rightNode[0], rightNode[1]-leftNode[2]),
            max(leftNode[1], rightNode[1]),
            min(leftNode[2], rightNode[2])]


# 세그먼트 트리 구성
def init(N, tree):
    for i in range(N-1, 0, -1):
        tree[i] = combine(tree[i<<1], tree[i<<1 | 1])


# index번째 인덱스를 value로 변경
def update(N, tree, index, value):
    index += N
    tree[index] = [0, value, value]

    while index > 1:
        index >>= 1
        tree[index] = combine(tree[index<<1], tree[index<<1 | 1])


# 구간 [left, right]에서 가장 큰 연속합 출력
def query(N, tree, left, right):
    left += N
    right += N
    resultL = tree[left]
    resultR = tree[right]

    while left <= right:
        if left & 1:
            resultL = combine(resultL, tree[left])
            left += 1
        if ~right & 1:
            resultR = combine(tree[right], resultR)
            right -= 1

        left >>= 1
        right >>= 1

    return combine(resultL, resultR)[0]


def main():
    N = int(input())
    A = list(map(int, input().split()))

    # 세그먼트 트리 기본 설정
    tree = [[0, 0, 0] for _ in range(N*2)]
    for i in range(N):
        tree[N+i] = [0, A[i], A[i]]
    init(N, tree)

    # 쿼리 처리
    M = int(input())
    for _ in range(M):
        t, a, b = map(int, input().split())
        if t == 1:
            update(N, tree, a-1, b)
        else:
            print(query(N, tree, a-1, b-1))


main()
