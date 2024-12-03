# 백준 1572

'''
세그먼트 트리의 리프 노드에는 해당 온도가 나온 빈도수를 저장하고,
가지 노드에는 각 자손 노드의 합을 저장한다.
query에서는 자식 노드에 저장된 값을 파악해서 중앙값을 확인한다.
'''

import sys
from collections import deque

input = sys.stdin.readline
MAX = 65536


# 온도가 index인 곳에 빈도수 value만큼 증가
def update(index, value):
    index += MAX
    tree[index] += value

    while index > 1:
        index >>= 1
        tree[index] = tree[index<<1] + tree[index<<1 | 1]


# index번째 값 반환
def query():
    index = (K+1)//2
    start = 1       # 현재 탐색하는 노드의 시작 날짜
    curIndex = 1    # 현재 탐색하는 세그먼트 트리의 인덱스

    while True:
        # 리프 노드에 도착한 경우
        if curIndex<<1 | 1 > MAX*2:
            break
        if start <= index < start+tree[curIndex<<1]:
            curIndex = curIndex<<1
        else:
            start = start+tree[curIndex<<1]
            curIndex = curIndex<<1 | 1
    
    return curIndex-MAX


# main 함수 ----------
N, K = map(int, input().split())

# 세그먼트 트리 초기화
tree = [0 for _ in range(2*MAX)]

# 쿼리 처리
result = 0
q = deque()

for i in range(K-1):
    data = int(input())
    update(data, 1)
    q.append(data)

for i in range(K-1, N):
    data = int(input())
    update(data, 1)
    q.append(data)

    result += query()

    update(q.popleft(), -1)

print(result)