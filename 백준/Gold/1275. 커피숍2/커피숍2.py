# 백준 1275

'''
세그먼트 트리를 이용해 i~j번째까지의 합을 구하자.
'''

import sys

input = sys.stdin.readline


# 세그먼트 트리 구성
def init():
    for i in range(N-1, 0, -1):
        tree[i] = tree[i<<1] + tree[i<<1 | 1]


# index번째 수의 값를 value로 변경
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


# main 함수 ----------
N, Q = map(int, input().split())

a = list(map(int, input().split()))

# 세그먼트 트리 설정
tree = [0 for _ in range(2*N)]
for i in range(N):
    tree[N+i] = a[i]
    
init()

# 쿼리 입력 및 처리
for _ in range(Q):
    x, y, a, b = map(int, input().split())
    print(query(min(x, y)-1, max(x, y)-1))
    update(a-1, b)
