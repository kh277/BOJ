# 백준 2268

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
        if left & 1:
            result += tree[left]
            left += 1
        if ~right & 1:
            result += tree[right]
            right -= 1
            
        left >>= 1
        right >>= 1
    
    return result


# main 함수 --------
N, M = map(int, input().split())

tree = [0 for _ in range(2*N)]

for i in range(M):
    a, b, c = map(int, input().split())
    if a == 0:
        print(query(min(b, c)-1, max(b, c)-1))
    else:
        update(b-1, c)