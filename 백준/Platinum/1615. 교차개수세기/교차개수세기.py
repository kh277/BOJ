# 백준 10999

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
ARRAY_TYPE = 'I'


# A[index]에 value만큼 값 추가
def update(N, tree, index, value):
    index += N
    tree[index] += value

    while index > 1:
        index >>= 1
        tree[index] = tree[index<<1] + tree[index<<1 | 1]


# 구간 [left, right]의 전체 합을 구하는 쿼리
def query(N, tree, left, right):
    result = 0
    left += N
    right += N

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
    N, M = map(int, input().split())
    edge = [[] for _ in range(N+1)]
    for _ in range(M):
        s, e = map(int, input().split())
        edge[s].append(e)

    # 정렬
    for i in range(1, N+1):
        if len(edge) > 1:
            edge[i].sort()

    size = 1<<N.bit_length()
    tree = array(ARRAY_TYPE, [0]) * (size*2)

    # 시작점 오름차순으로 쿼리 처리
    cross = 0
    for i in range(N+1):
        if len(edge[i]) != 0:
            for curE in edge[i]:
                update(size, tree, curE, 1)
                cross += query(size, tree, curE+1, N+1)

    print(cross)
    return


main()
