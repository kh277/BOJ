# 백준 1306

'''
연속하는 2M-1개의 범위에 대해 최대값을 구해야 하며,
이 쿼리를 N-M번 구해야 한다.

세그먼트 트리를 통해 2M-1개의 수를 유지하면서 최소값을 찾는다.
슬라이딩 윈도우를 이용하기 위해 가장 오래된 값을 다음 값으로 대체한 뒤 다시 쿼리를 수행하면 된다.
'''

import sys

input = sys.stdin.readline

# 세그먼트 트리 구성
def init(N, tree):
    for i in range(N-1, 0, -1):
        tree[i] = max(tree[i<<1], tree[i<<1 | 1])


# index번째 인덱스를 value로 변경
def update(N, tree, index, value):
    index += N
    tree[index] = value
    
    while index > 1:
        index >>= 1
        tree[index] = max(tree[index<<1], tree[index<<1 | 1])


# left ~ right까지 중 최대값 계산
def query(N, tree):
    return tree[1]


def solve():
    # 세그먼트 트리 초기 설정
    L = 2*M-1
    window = [0 for i in range(2*L)]
    for i in range(L):
        window[i+L] = A[i]
    init(L, window)
    
    # 쿼리 처리
    result = []
    result.append(query(L, window))
    index = 0
    for i in range(L, N):
        update(L, window, index, A[i])
        result.append(query(L, window))
        index = (index+1) % L
        
    return result


# main 함수 ----------
N, M = map(int, input().split())
A = list(map(int, input().split()))

print(*solve())