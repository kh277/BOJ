# 백준 3572

'''
tree[i] = 현재 구간에서 추가할 수 있는 가장 큰 알림판 길이
'''

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


# 크기가 N인 세그먼트 트리 빌드 및 [0, index]번까지만 value로 채우기
def build(N, index, value):
    tree = array('i', [0]) * (N*2)
    for i in range(index):
        tree[N+i] = value

    for index in range(N-1, 0, -1):
        tree[index] = max(tree[index<<1], tree[index<<1 | 1])

    return tree


# index번째 값을 value만큼 감소
def update(N, tree, index, value):
    # index += N
    tree[index] -= value

    while index > 1:
        index >>= 1
        tree[index] = max(tree[index<<1], tree[index<<1 | 1])


# tree에 value 길이를 넣을 수 있는 최초 인덱스 반환
def query(N, tree, value):
    index = 1

    while index < N:
        left = index<<1
        right = left | 1

        if tree[left] >= value:
            index = left
        elif tree[right] >= value:
            index = right
        else:
            return -1

    return index


def main():
    Y, X, Q = map(int, input().split())
    Y = min(Y, Q)
    size = 1<<Y.bit_length()
    tree = build(size, Y, X)

    for _ in range(Q):
        value = int(input())

        # 알림판을 추가할 수 있는 최초 위치 찾기
        pos = query(size, tree, value)

        # 알림판 추가 연산
        if pos != -1:
            update(size, tree, pos, value)
            print(pos-size+1)
        else:
            print(-1)


main()
