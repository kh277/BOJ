# 백준 10999

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**10


# [start, end] 범위의 세그먼트 트리 생성
def build(tree, A, curV, start, end):
    # 리프 노드인 경우
    if start == end:
        tree[curV] = A[start]
        return tree[curV]

    mid = (start+end)//2
    tree[curV] = build(tree, A, curV<<1, start, mid) + build(tree, A, curV<<1 | 1, mid+1, end)
    return tree[curV]


# 세그먼트 트리의 [start, end] 범위에서 [qLeft, qRight] 범위의 합 반환
def query(tree, lazy, curV, start, end, qLeft, qRight):
    # 현재 노드의 lazy 먼저 처리
    prop(tree, lazy, curV, start, end)

    # 겹치는 구간이 없는 경우
    if qLeft > end or qRight < start:
        return 0

    # 전체 범위인 경우
    if qLeft <= start and end <= qRight:
        return tree[curV]

    mid = (start+end)//2
    return query(tree, lazy, curV<<1, start, mid, qLeft, qRight) + query(tree, lazy, curV<<1 | 1, mid+1, end, qLeft, qRight)


def prop(tree, lazy, curV, start, end):
    # 업데이트가 필요한 경우
    if lazy[curV] != 0:
        tree[curV] += (end-start+1) * lazy[curV]

        # 리프 노드가 아닌 경우
        if start != end:
            lazy[curV<<1] += lazy[curV]
            lazy[curV<<1 | 1] += lazy[curV]

        lazy[curV] = 0


def lazyUpdate(tree, lazy, curV, start, end, qLeft, qRight, value):
    # lazy값이 남아있으면 전파
    prop(tree, lazy, curV, start, end)

    if qLeft > end or qRight < start:
        return
    
    if qLeft <= start and end <= qRight:
        tree[curV] += (end-start+1) * value

        # 리프 노드가 아니라면
        if start != end:
            lazy[curV<<1] += value
            lazy[curV<<1 | 1] += value
        return

    mid = (start+end)//2
    lazyUpdate(tree, lazy, curV<<1, start, mid, qLeft, qRight, value)
    lazyUpdate(tree, lazy, curV<<1 | 1, mid+1, end, qLeft, qRight, value)
    tree[curV] = tree[curV<<1] + tree[curV<<1 | 1]


def main():
    N, M, K = map(int, input().split())
    A = []
    for _ in range(N):
        A.append(int(input()))
    size = 4*N
    tree = [0] * size
    lazy = [0] * size

    # 세그먼트 트리 빌드
    build(tree, A, 1, 0, N-1)

    # 쿼리 처리
    for _ in range(M+K):
        q = list(map(int, input().split()))
        # 1 : 구간 업데이트 쿼리
        if q[0] == 1:
            lazyUpdate(tree, lazy, 1, 0, N-1, q[1]-1, q[2]-1, q[3])

        # 2: 구간 합 쿼리
        else:
            print(query(tree, lazy, 1, 0, N-1, q[1]-1, q[2]-1))


main()
