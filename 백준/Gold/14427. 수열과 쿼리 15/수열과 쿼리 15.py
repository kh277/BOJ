# 백준 14427

'''
수열 전체에서 최소값의 인덱스를 출력하는 문제이다.
따라서 세그먼트 트리에 각 구간 별 최소값 및 최소값의 인덱스를 저장하고
루트 노드에 저장된 값을 반환하면 된다.
'''


import sys

input = sys.stdin.readline


# 세그먼트 트리 구성
def init():
    for i in range(N-1, 0, -1):
        # [최소값, 최소값의 인덱스] 순서로 저장
        if tree[i<<1][0] > tree[i<<1 | 1][0]:
            tree[i] = tree[i<<1 | 1]
        elif tree[i<<1][0] == tree[i<<1 | 1][0]:
            tree[i] = [tree[i<<1][0], min(tree[i<<1][1], tree[i<<1 | 1][1])]
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
        elif tree[index<<1][0] == tree[index << 1 | 1][0]:
            tree[index] = [tree[index<<1][0], min(tree[index<<1][1], tree[index<<1 | 1][1])]
        else:
            tree[index] = tree[index<<1]


# 수열 전체에서 최소값의 인덱스 반환
def query():
    return tree[1][1]+1


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
    command = list(map(int, input().split()))
    if command[0] == 1:
        update(command[1]-1, command[2])
    else:
        print(query())