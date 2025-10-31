# 백준 12741

'''
1 i j : 구간 [i, j)의 원소가 비내림차순인지 체크
2 i j : swap(A[i], A[j])
오름차순일 경우 1, 비내림차순일 경우 0을 저장하는 배열을 만들고,
세그먼트 트리로 구간 [i, j]의 합이 0인지 여부를 판단하면 된다.
swap 처리를 할 때마다 배열의 값을 수정해 주어야 한다.
'''

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
ARRAY_TYPE = 'I'


# 크기가 N인 세그먼트 트리 빌드
def build(N, A):
    tree = array(ARRAY_TYPE, [0]) * (N*2)
    for i in range(len(A)):
        tree[N+i] = A[i]

    for index in range(N-1, 0, -1):
        tree[index] = tree[index<<1] + tree[index<<1 | 1]

    return tree


# index번째 값을 value로 변경
def update(N, tree, index, value):
    index += N
    tree[index] = value

    while index > 1:
        index >>= 1
        tree[index] = tree[index<<1] + tree[index<<1 | 1]


# 0-base, 구간 [left, right]의 전체 합을 구하는 쿼리
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
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    B = array(ARRAY_TYPE, [0]) * N

    for i in range(N-1):
        if A[i] > A[i+1]:
            B[i] = 1

    size = 1 << (N.bit_length())
    tree = build(size, B)

    for _ in range(Q):
        a, b, c = map(int, input().split())
        if a == 1:
            if b == c:
                print('CS204')
            elif query(size, tree, b-1, c-2) == 0:
                print('CS204')
            else:
                print('HSS090')
        else:
            A[b-1], A[c-1] = A[c-1], A[b-1]
            candidate = []
            for i in (b-2, c-2, b-1, c-1):
                if 0 <= i < N-1:
                    candidate.append(i)
            for i in candidate:
                if A[i] > A[i+1]:
                    update(size, tree, i, 1)
                else:
                    update(size, tree, i, 0)


main()
