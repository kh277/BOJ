# 백준 2042

'''
세그먼트 트리를 비재귀 형태로 구현했다.
'''

import sys

input = sys.stdin.readline


# 세그먼트 트리 구성
def init():
    for i in range(N-1, 0, -1):
        tree[i] = tree[i<<1] + tree[i<<1 | 1]


# index번째 인덱스를 value로 변경
def update(index, value):
    index += N
    tree[index] = value
    
    while index > 1:
        index >>= 1
        tree[index] = tree[index<<1] + tree[index<<1 | 1]


# left ~ right까지의 합 계산
def query(left, right):
    result = 0
    left += N
    right += N
    
    while left <= right:
        # left가 홀수라면
        if left & 1:
            result += tree[left]
            left += 1
        # right가 홀수라면
        if ~right & 1:
            result += tree[right]
            right -= 1
            
        left >>= 1
        right >>= 1
    
    return result


# main 함수 ----------
N, M, K = map(int, input().split())

a = []
for _ in range(N):
    a.append(int(input()))

# 세그먼트 트리 설정
tree = [0 for _ in range(2*N)]
for i in range(N):
    tree[N+i] = a[i]
    
init()

# 쿼리 입력 및 처리
for _ in range(M+K):
    x, y, z = map(int, input().split())
    if x == 1:
        update(y-1, z)
    else:
        print(query(y-1, z-1))
