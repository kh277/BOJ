# 백준 11505

import sys
import math

input = sys.stdin.readline


# 배열 a와 노드가 저장할 범위 start~end를 입력받아 tree 구성
def init(a, tree, node, start, end):
    # 리프 노드의 경우
    if start == end:
        tree[node] = a[start]

    # 재귀를 통해 자식 노드 구성
    else:
        init(a, tree, node*2, start, (start+end)//2)
        init(a, tree, node*2+1, (start+end)//2+1, end)
        tree[node] = (tree[node*2] * tree[node*2+1]) % 1000000007


# left ~ right 까지의 합 계산
def query(tree, node, start, end, left, right):
    # 구하는 값이 노드에 저장된 start~end 외부에 있는 경우
    if left > end or right < start:
        return 1
    # 구하는 값이 노드에 저장된 start~end를 포함하는 경우
    if left <= start and end <= right:
        return tree[node]
    
    # 구하는 값이 start~end 범위에 걸치는 경우 -> 재귀
    leftSum = query(tree, node*2, start, (start+end)//2, left, right)
    rightSum = query(tree, node*2+1, (start+end)//2+1, end, left, right)
    
    return (leftSum * rightSum) % 1000000007


def update_tree(tree, node, start, end, index):
    # index가 노드에 저장된 start~end 외부에 있는 경우 
    if index < start or index > end:
        return tree[node]
    
    # 리프 노드가 아닌 경우 -> 재귀
    if start != end:
        leftSum = update_tree(tree, node*2, start, (start+end)//2, index)
        rightSum = update_tree(tree, node*2+1, (start+end)//2+1, end, index)
        tree[node] = (leftSum * rightSum) % 1000000007
        return tree[node]
    
    # 리프 노드인 경우
    else:
        tree[node] = a[index]
        return a[index]


# a[index]의 값을 val로 변경하는 함수
def update(a, tree, n, index, val):
    a[index] = val
    update_tree(tree, 1, 0, n-1, index)


# main 함수 ----------
N, M, K = map(int, input().split())

a = []
for _ in range(N):
    a.append(int(input()))

# 세그먼트 트리 설정
tree = [0 for _ in range(2**(math.ceil(math.log(N, 2)+1)))]
init(a, tree, 1, 0, N-1)

# 쿼리 입력 및 처리
for _ in range(M+K):
    x, y, z = map(int, input().split())
    if x == 1:
        update(a, tree, N, y-1, z)
    else:
        print(query(tree, 1, 0, N-1, y-1, z-1))

