# 백준 16978

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def init(tree):
    for i in range(N-1, 0, -1):
        tree[i] = tree[i<<1] + tree[i<<1 | 1]


def update(tree, index, value):
    index += N
    tree[index] = value
    
    while index > 1:
        index >>= 1
        tree[index] = tree[index<<1] + tree[index<<1 | 1]


def query(tree, left, right):
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


def solve():
    # 세그먼트 트리 기본 설정
    tree = [0 for _ in range(2*N)]
    for i in range(N):
        tree[i+N] = A[i]
    init(tree)

    query2.sort(key= lambda x: x[0])
    query1.reverse()
    result = [0 for _ in range(len(query2))]

    # 쿼리 적용 시점 순서 기준으로 처리
    appliedQuery = 0
    for i in range(len(query2)):
        curQuery, start, end, query2Count = query2[i]

        # curQuery까지 적용
        while curQuery > appliedQuery:
            update(tree, query1[-1][0]-1, query1[-1][1])
            appliedQuery += 1
            query1.pop()
        
        result[query2Count] = query(tree, start-1, end-1)
    
    return result


# main 함수 --------
N = int(input())
A = list(map(int, input().split()))

M = int(input())
query1 = []
query2 = []
query2Count = 0
for i in range(M):
    queryType, *q = map(int, input().split())
    if queryType == 1:
        query1.append(q)
    else:
        query2.append(q + [query2Count])
        query2Count += 1

for i in solve():
    print(i)