# 백준 10868

'''
세그먼트 트리를 구성할 때 작은 값을 저장하도록 하면 된다.
'''

import sys

input = sys.stdin.readline
INF = 10e10

# 세그먼트 트리 구성
def init():
    for i in range(N-1, 0, -1):
        tree[i] = min(tree[i<<1], tree[i<<1 | 1])


# index번째 인덱스를 value로 변경
def update(index, value):
    index += N
    tree[index] = value
    
    while index > 1:
        index >>= 1
        tree[index] = min(tree[i<<1], tree[i<<1 | 1])


# left ~ right까지의 합 계산
def query(left, right):
    result = INF
    left += N
    right += N
    
    while left <= right:
        # left가 홀수라면
        if left & 1:
            result = min(tree[left], result)
            left += 1
        # right가 홀수라면
        if ~right & 1:
            result = min(tree[right], result)
            right -= 1
            
        left >>= 1
        right >>= 1
    
    return result


# main 함수 ----------
N, M = map(int, input().split())

# 세그먼트 트리 초기화
tree = [0 for _ in range(2*N)]
for i in range(N):
    temp = int(input())
    tree[i+N] = temp

# 세그먼트 트리 구성
init()

# 쿼리 처리
for i in range(M):
    l, r = map(int, input().split())
    print(query(l-1, r-1))
