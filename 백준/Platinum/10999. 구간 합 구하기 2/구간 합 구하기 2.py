# 백준 10999

import sys

input = sys.stdin.readline


def build(N, A):
    tree = [0] * (N*2)
    for i in range(len(A)):
        tree[N+i] = A[i]

    for i in range(N-1, 0, -1):
        tree[i] = tree[i<<1] + tree[i<<1 | 1]
    
    return tree


# index노드가 담당하는 구간 전체에 쿼리 적용
def apply(N, tree, lazy, length, index, value):
    tree[index] += value * length[index]

    # 리프 노드가 아니라면
    if index < N:
        lazy[index] += value


# A[index] 부모 노드들의 미적용 lazy 전파
def push(N, tree, lazy, length, index):
    for s in range(N.bit_length()-1, 0, -1):
        nextI = index >> s

        # 미적용 lazy가 있는 경우
        if lazy[nextI]:
            apply(N, tree, lazy, length, nextI<<1, lazy[nextI])
            apply(N, tree, lazy, length, nextI<<1 | 1, lazy[nextI])
            lazy[nextI] = 0


# A[index] 부모 노드들의 tree 갱신
def pull(N, tree, lazy, length, index):
    while index > 1:
        index >>= 1
        tree[index] = tree[index<<1] + tree[index<<1 | 1] + lazy[index] * length[index]


# 구간 [left, right]에 value값 더하기
def lazyUpdate(N, tree, lazy, length, left, right, value):
    left += N
    right += N

    # 업데이트 전 양쪽 끝 노드 경로의 lazy 전파
    prefL = left
    suffR = right
    push(N, tree, lazy, length, prefL)
    push(N, tree, lazy, length, suffR)

    while left <= right:
        if left & 1:
            apply(N, tree, lazy, length, left, value)
            left += 1
        if ~right & 1:
            apply(N, tree, lazy, length, right, value)
            right -= 1
        left >>= 1
        right >>= 1
    
    # 업데이트 후 위로 올라오면서 부모 값 갱신
    pull(N, tree, lazy, length, prefL)
    pull(N, tree, lazy, length, suffR)


# 구간 [left, right]의 합 구하기
def query(N, tree, lazy, length, left, right):
    left += N
    right += N
    push(N, tree, lazy, length, left)
    push(N, tree, lazy, length, right)

    result = 0
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
    N, M, K = map(int, input().split())
    A = []
    for _ in range(N):
        A.append(int(input()))

    size = 1<<N.bit_length()
    lazy = [0] * (size*2)

    # length : 각 노드가 담당하는 구간의 길이
    length = [1] * (size*2)
    for i in range(size-1, 0, -1):
        length[i] = length[i<<1] + length[i<<1 | 1]

    # 세그먼트 트리 빌드
    tree = build(size, A)

    # 쿼리 처리
    for _ in range(M+K):
        q = list(map(int, input().split()))
        # 1 : 구간 업데이트 쿼리
        if q[0] == 1:
            lazyUpdate(size, tree, lazy, length, q[1]-1, q[2]-1, q[3])

        # 2: 구간 합 쿼리
        else:
            print(query(size, tree, lazy, length, q[1]-1, q[2]-1))


main()
