# 백준 14428

'''
i~j까지 중 최소값을 출력하는 것이 아니라 최소값의 인덱스를 출력해야 한다.
따라서 세그먼트 트리를 이차원으로 유지하여 최소값과 그 인덱스를 함께 저장하자.
'''


import sys

input = sys.stdin.readline


# 세그먼트 트리 구성
def init():
    for i in range(N-1, 0, -1):
        # [최소값, 최소값의 인덱스] 순서로 저장
        if tree[i<<1][0] > tree[i<<1 | 1][0]:
            tree[i] = tree[i<<1 | 1]
        else:
            tree[i] = tree[i<<1]


# index번째 인덱스를 value로 변경
def update(index, value):
    index += N
    tree[index] = [value, index-N]
    
    while index > 1:
        index >>= 1
        if tree[index<<1][0] > tree[index<<1 | 1][0]:
            tree[index] = tree[index<<1 | 1]
        else:
            tree[index] = tree[index<<1]


# left ~ right까지의 최소값 계산
def query(left, right):
    result = left
    left += N
    right += N
    
    while left <= right:
        # left가 홀수라면
        if left & 1:
            if tree[result+N][0] > tree[left][0]:
                result = tree[left][1]
            elif tree[result+N][0] == tree[left][0]:
                result = min(tree[result+N][1], tree[left][1])
            left += 1
        
        # right가 짝수라면
        if ~right & 1:
            if tree[result+N][0] > tree[right][0]:
                result = tree[right][1]
            elif tree[result+N][0] == tree[right][0]:
                result = min(tree[result+N][1], tree[right][1])
            right -= 1
            
        left >>= 1
        right >>= 1
    
    return result+1


# main 함수 ----------
N = int(input())
A = list(map(int, input().split()))
M = int(input())

# 세그먼트 트리 초기화
tree = [0 for _ in range(2*N)]
for i in range(N):
    tree[i+N] = [A[i], i]
init()

# 쿼리 처리
for _ in range(M):
    command, i, j = map(int, input().split())
    if command == 1:
        update(i-1, j)
    else:
        print(query(i-1, j-1))