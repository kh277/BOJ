# 백준 11505


import sys

input = sys.stdin.readline


# 세그먼트 트리 구성
def init():
    for i in range(N-1, 0, -1):
        tree[i] = (tree[i<<1] * tree[i<<1 | 1]) % 1000000007


# index번째 인덱스를 value로 변경
def update(index, value):
    index += N
    tree[index] = value
    
    while index > 1:
        index >>= 1
        tree[index] = (tree[index<<1] * tree[index<<1 | 1]) % 1000000007


# left ~ right까지의 합 계산
def query(left, right):
    result = 1
    left += N
    right += N
    
    while left <= right:
        # left가 홀수라면
        if left & 1:
            result = (result * tree[left]) % 1000000007
            left += 1
        # right가 홀수라면
        if ~right & 1:
            result = (result * tree[right]) % 1000000007
            right -= 1
            
        left >>= 1
        right >>= 1
    
    return result


# main 함수 ----------
N, M, K = map(int, input().split())

# 세그먼트 트리 설정
tree = [0 for _ in range(2*N)]

for i in range(N):
    tree[i+N] = int(input())

init()

# 쿼리 입력 및 처리
for _ in range(M+K):
    x, y, z = map(int, input().split())
    if x == 1:
        update(y-1, z)
    else:
        print(query(y-1, z-1))