# 백준 9345

'''
두 원소에 대해 swap 쿼리, 구간에 대해 DVD 번호가 다 존재하는지 확인하는 쿼리
10만개의 원소에 대해 위의 두 쿼리를 최대 5만번 수행해야 하므로 세그먼트 트리를 이용해야 한다.

각 노드에는 [최소값, 최대값]을 저장하고,
쿼리를 처리할 때 구간 내의 최소값, 최대값이 일치하는지 확인하면 된다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10e7


def square(num):
    result = 1
    while True:
        if result >= num:
            return result
        result *= 2


# 세그먼트 트리 구성
def init(tree):
    for i in range(N):
        tree[i+N] = [i, i]      # [최소값, 최대값] 순서로 저장

    for i in range(N-1, 0, -1):
        tree[i][0] = min(tree[i<<1][0], tree[i<<1 | 1][0])
        tree[i][1] = max(tree[i<<1][1], tree[i<<1 | 1][1])

    return tree


# index번째 인덱스의 값을 value로 변경
def update(tree, index, value):
    index += N
    tree[index] = [value, value]
    
    while index > 1:
        index >>= 1
        tree[index][0] = min(tree[index<<1][0], tree[index<<1 | 1][0])
        tree[index][1] = max(tree[index<<1][1], tree[index<<1 | 1][1])


# 범위 [left, right]에 값이 다 있는지 체크
def query(tree, left, right):
    numRange = [left, right]
    result = [INF, -INF]
    left += N
    right += N

    while left <= right:
        if left & 1:
            result[0] = min(result[0], tree[left][0])
            result[1] = max(result[1], tree[left][1])
            left += 1
        # right가 짝수라면
        if ~right & 1:
            result[0] = min(result[0], tree[right][0])
            result[1] = max(result[1], tree[right][1])
            right -= 1
            
        left >>= 1
        right >>= 1

    if result[0] == numRange[0] and result[1] == numRange[1]:
        return 'YES'
    else:
        return 'NO'


# main 함수 ----------
T = int(input())
for _ in range(T):
    tempN, K = map(int, input().split())
    N = square(tempN)
    
    # tree 기본 설정
    tree = [[0, 0] for _ in range(2*N)]
    tree = init(tree)

    # 쿼리 처리
    for _ in range(K):
        Q, A, B = map(int, input().split())
        if Q == 0:
            swapA = tree[A+N][0]
            swapB = tree[B+N][0]
            update(tree, B, swapA)
            update(tree, A, swapB)
        else:
            print(query(tree, A, B))