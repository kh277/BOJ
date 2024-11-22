# 백준 1321

'''
세그먼트 트리의 리프 노드에는 각 부대에 있는 인원수를,
가지 노드에는 각 자손 노드의 합을 저장한다.
query에서는 자식 노드에 저장된 값을 파악해서 i번째 인원의 부대를 확인한다.
'''

import sys

input = sys.stdin.readline


# num 이상인 2의 제곱수 반환
def change(num):
    temp = 1
    while True:
        if temp >= num:
            return temp
        else:
            temp *= 2


# 세그먼트 트리 구성
def init():
    for i in range(N-1, 0, -1):
        tree[i] = tree[i<<1] + tree[i<<1 | 1]


# index번째 부대에 value 값을 더하기
def update(index, value):
    index += N
    tree[index] += value
    
    while index > 1:
        index >>= 1
        tree[index] = tree[index<<1] + tree[index<<1 | 1]


# index번째 군인의 부대 파악
def query(index):
    start = 1       # 현재 탐색하는 군인들의 시작 번호
    curIndex = 1    # 현재 탐색하는 세그먼트 트리의 인덱스

    while True:
        # 리프 노드에 도착한 경우
        if curIndex<<1 | 1 > N*2:
            break
        if start <= index < start+tree[curIndex<<1]:
            curIndex = curIndex<<1
        else:
            start = start+tree[curIndex<<1]
            curIndex = curIndex<<1 | 1
    
    return curIndex-N+1


# main 함수 ----------
part = int(input())
N = change(part)
camp = list(map(int, input().split()))

# 세그먼트 트리 초기화
tree = [0 for _ in range(2*N)]
for i in range(part):
    tree[N+i] = camp[i]
init()

# 쿼리 처리
M = int(input())
for _ in range(M):
    q = list(map(int, input().split()))
    if q[0] == 1:
        update(q[1]-1, q[2])
    else:
        print(query(q[1]))