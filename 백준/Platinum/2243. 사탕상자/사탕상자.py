# 백준 2243

'''
1 i : i번째로 큰 사탕을 꺼낸다.
2 i j : 맛의 등급이 i인 사탕을 j개 넣는다.
빈 사탕상자에서 시작해서 위의 쿼리 N회를 처리할 때,
사탕상자에서 꺼낼 때 맛의 번호를 출력하면 된다.

사탕의 맛이 최대 1~100만까지라고 했으니 크기가 100만인 배열을 만들어 각 사탕의 맛에 대한 수를 저장하자.
그리고 세그트리에 자식 노드에 있는 사탕의 개수를 저장하자.
'''

import sys

input = sys.stdin.readline


# 맛이 taste인 사탕의 개수를 value만큼 변경하는 연산
def update(taste, value):
    taste += N
    tree[taste] += value
    
    while taste > 1:
        taste >>= 1
        tree[taste] = tree[taste<<1] + tree[taste<<1 | 1]


# grade번째 사탕을 1개 꺼내는 연산
def query(grade):
    start = 1
    end = tree[1]

    curIndex = 1
    while True:
        tree[curIndex] -= 1

        # 리프 노드에 도달한 경우
        if curIndex<<1 | 1 > N*2:
            break

        # 왼쪽 자식 노드에 해당 사탕이 있는 경우
        if start <= grade < start+tree[curIndex<<1]:
            end = start+tree[curIndex<<1]-1
            curIndex = curIndex<<1
        # 오른쪽 자식 노드에 해당 사탕이 있는 경우 
        else:
            start = start+tree[curIndex<<1]
            curIndex = curIndex<<1 | 1
    
    return curIndex-N


# main 함수 ----------
N = 1048576     # 최대가 100만이지만, 비재귀로 구현하기 위해 완전이진트리로 생성
Q = int(input())

tree = [0 for _ in range(N*2)]

for _ in range(Q):
    command = list(map(int, input().split()))
    # 사탕을 꺼내는 쿼리
    if command[0] == 1:
        print(query(command[1]))
    # 사탕의 개수를 수정하는 쿼리
    else:
        update(command[1], command[2])
