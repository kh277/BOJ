# 백준 14438

'''
i~j까지 중 최소값 출력하면 된다.
따라서 세그먼트 트리에 각 구간 별 최소값을 저장하자.
'''


import sys

input = sys.stdin.readline

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
        tree[index] = min(tree[index<<1], tree[index<<1 | 1])


# left ~ right 중 최소값 반환
def query(left, right):
    result = 10e10
    left += N
    right += N
    
    while left <= right:
        if left & 1:
            result = min(result, tree[left])
            left += 1
        if ~right & 1:
            result = min(result, tree[right])
            right -= 1
            
        left >>= 1
        right >>= 1
    
    return result


# main 함수 ----------
N = int(input())
A = list(map(int, input().split()))
M = int(input())

# 세그먼트 트리 초기화
tree = [0 for _ in range(2*N)]
for i in range(N):
    tree[i+N] = A[i]
init()

# 쿼리 처리
for _ in range(M):
    command, i, j = map(int, input().split())
    if command == 1:
        update(i-1, j)
    else:
        print(query(i-1, j-1))