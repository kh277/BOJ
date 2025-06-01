# 백준 13557

'''
구조체 세그 응용 문제. 두 구간이 겹칠 때와 겹치지 않을 때, 두 가지 경우로 나누어서 풀면 된다.
각 노드는 [구간의 왼쪽 접두사 포함 최대 연속합, 구간의 오른쪽 접미사 포함 최대 연속합, 구간 내 최대 연속합, 구간 내 총합] 저장.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**11


def square(num):
    result = 1
    while True:
        if result >= num:
            return result
        result *= 2


# left, right 노드 병합
def combine(leftNode, rightNode):
    return [max(leftNode[0], leftNode[3]+rightNode[0]),
            max(rightNode[1], leftNode[1]+rightNode[3]),
            max(leftNode[2], rightNode[2], leftNode[1]+rightNode[0]),
            leftNode[3] + rightNode[3]]


# 크기가 N인 구조체 세그트리 빌드
def build(N, A):
    tree = [[0, 0, 0, 0] for _ in range(N*2)]
    for i in range(len(A)):
        tree[N+i] = [A[i], A[i], A[i], A[i]]

    for i in range(N-1, 0, -1):
        left = i<<1
        right = i<<1 | 1

        tree[i] = combine(tree[left], tree[right])
    
    return tree


# index번째 노드에 값 추가 및 노드 갱신
def update(N, tree, index, value):
    index += N
    for i in range(4):
        tree[index][i] += value

    while index > 1:
        index >>= 1
        tree[index] = combine(tree[index<<1], tree[index<<1 | 1])


# 구간 [left, right]의 연속합 노드 반환
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

    return combine(resultL, resultR)



def main():
    N = int(input())
    size = square(N)
    num = list(map(int, input().split()))
    tree = build(size, num)

    M = int(input())
    for _ in range(M):
        x1, y1, x2, y2 = map(int, input().split())
        # 두 구간이 분리된 경우
        if y1 <= x2:
            range1 = query(size, tree, x1-1, y1-1)
            range2 = query(size, tree, y1-1, x2-1)
            range3 = query(size, tree, x2-1, y2-1)
            print(range1[1] + range2[3] + range3[0] - num[y1-1] - num[x2-1])
        # 두 구간이 겹치는 경우
        else:
            range1 = query(size, tree, x1-1, x2-1)
            range2 = query(size, tree, x2-1, y1-1)
            range3 = query(size, tree, y1-1, y2-1)
            case1 = range1[1] + range2[0] - num[x2-1]
            case2 = range1[1] + range2[3] + range3[0] - num[x2-1] - num[y1-1]
            case3 = range2[2]
            case4 = range2[1] + range3[0] - num[y1-1]
            print(max(case1, case2, case3, case4))


main()
