# 백준 12899

'''
2243번과 유사한 문제.
'''

import sys

input = sys.stdin.readline


# 수 X를 추가하는 연산
def update(X):
    X += N
    tree[X] += 1
    
    while X > 1:
        X >>= 1
        tree[X] = tree[X<<1] + tree[X<<1 | 1]


# grade번째로 수를 찾고 그 수를 삭제하는 연산
def query(grade):
    start = 1

    curIndex = 1
    while True:
        tree[curIndex] -= 1

        # 리프 노드에 도달한 경우
        if curIndex<<1 | 1 > N*2:
            break

        # 왼쪽 자식 노드에 해당 사탕이 있는 경우
        if start <= grade < start+tree[curIndex<<1]:
            curIndex = curIndex<<1
        # 오른쪽 자식 노드에 해당 사탕이 있는 경우 
        else:
            start = start+tree[curIndex<<1]
            curIndex = curIndex<<1 | 1
    
    return curIndex-N


# main 함수 ----------
N = 2097152     # 최대가 200만이지만, 비재귀로 구현하기 위해 완전이진트리로 생성
Q = int(input())

tree = [0 for _ in range(N*2)]

for _ in range(Q):
    T, X = list(map(int, input().split()))
    # X를 추가하는 쿼리
    if T == 1:
        update(X)
    # X번째 작은 수를 삭제하는 쿼리
    else:
        print(query(X))
