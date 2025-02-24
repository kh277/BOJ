# 백준 25639

'''
트리를 imos법으로 구성할 경우 구간 내에서 연속합의 최대를 구하는 쿼리가 됨.
-> 금광세그 기본 문제.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**15


def square(num):
    result = 1
    while True:
        if result >= num:
            return result
        result *= 2


# 해당 노드를 num으로 초기화
def nodeInit(num):
    return [num, num, num, num]


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


# index번째 인덱스를 value로 변경
def update(N, tree, index, value):
    index += N
    tree[index] = nodeInit(value)

    while index > 1:
        index >>= 1
        tree[index] = combine(tree[index<<1], tree[index<<1 | 1])


# 구간 [left, right]에서 가장 큰 연속합 출력
def query(N, tree, left, right):
    resultL = nodeInit(-INF)
    resultR = nodeInit(-INF)
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
    tree = [nodeInit(0) for _ in range(N*2)]
    for i in range(1, tempN):
        tree[N+i] = nodeInit(A[i]-A[i-1])

    init(N, tree)

    # 쿼리 처리
    M = int(input())
    for _ in range(M):
        t, a, b = map(int, input().split())
        if t == 1:
            if a > 1:
                update(N, tree, a-1, b-A[a-2])
            if a < tempN:
                update(N, tree, a, A[a]-b)
            A[a-1] = b
        else:
            if a == b:
                print(0)
            else:
                print(max(0, query(N, tree, a, b-1)))


main()
