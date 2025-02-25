# 백준 2849

'''
각 노드에 [구간 내 접두사 포함 최대 점수, 구간 내 접미사 포함 최대 점수,
    구간 내 최대 점수, 구간의 길이, 구간 시작 안무, 구간 끝 안무] 저장.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


# left구간, right구간 병합 처리
def combine(leftNode, rightNode):
    result = [leftNode[0], rightNode[1], max(leftNode[2], rightNode[2]),
            leftNode[3]+rightNode[3], leftNode[4], rightNode[5]]

    # left 구간과 + right 구간 연결이 가능한 경우
    if leftNode[5] != rightNode[4]:
        # left 전구간이 완벽한 경우
        if leftNode[0] == leftNode[3]:
            result[0] += rightNode[0]
        # right 전구간이 완벽한 경우
        if rightNode[1] == rightNode[3]:
            result[1] += leftNode[1]

        result[2] = max(result[2], leftNode[1]+rightNode[0])

    result[2] = max(result[0], result[1], result[2])
    return result


def init(N, tree):
    for i in range(N-1, 0, -1):
        tree[i] = combine(tree[i<<1], tree[i<<1 | 1])


# index번째 안무를 value로 변경
def update(N, tree, index, value):
    index += N
    tree[index] = [1, 1, 1, 1, value, value]

    while index > 1:
        index >>= 1
        tree[index] = combine(tree[index<<1], tree[index<<1 | 1])


# 구간 [left, right]에서 가장 큰 점수 반환
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

    return combine(resultL, resultR)[2]


def main():
    N, Q = map(int, input().split())

    # 세그먼트 트리 기본 설정
    tree = [[1, 1, 1, 1, 'L', 'L'] for _ in range(N*2)]
    init(N, tree)

    # 쿼리 처리
    for _ in range(Q):
        a = int(input())
        if tree[N+a-1][4] == 'L':
            update(N, tree, a-1, 'R')
        else:
            update(N, tree, a-1, 'L')
        print(query(N, tree, 0, N-1))


main()