# 백준 16975

'''
수열 A을 기준으로 세그먼트 트리를 만든다. (0~N-1)
세그먼트 트리의 리프 노드에는 [i, N-1]에 대한 변화량을 저장한다.
tree[i]의 값은 A[i] + (구간 [0, i]의 총합)을 구하는 것과 같다.

= 점 쿼리, 구간 업데이트
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


# num이상의 2의 제곱수 반환
def square(num):
    result = 1
    while True:
        if result >= num:
            return result
        result *= 2


# 세그먼트 트리 구성
def init(N, tree):
    for i in range(N-1, 0, -1):
        tree[i] = tree[i<<1] + tree[i<<1 | 1]


# tree[index]에 value만큼 값 추가, 트리 갱신
def update(N, tree, index, value):
    index += N
    tree[index] += value
    
    while index > 1:
        index >>= 1
        tree[index] = tree[index<<1] + tree[index<<1 | 1]


# 구간 [left, right]에서 리프 노드의 총합 반환
def query(N, tree, left, right):
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
N = int(input())
tempN = square(N+1)

# 초기 설정
tree = [0 for _ in range(2*tempN)]
a = list(map(int, input().split()))


# 쿼리 처리
M = int(input())
for _ in range(M):
    q = list(map(int, input().split()))

    # 1 i j k : 구간 합 쿼리
    if q[0] == 1:
        update(tempN, tree, q[1], q[3])
        if q[2] <= N-1:
            update(tempN, tree, q[2]+1, -q[3])
    # 2 x : 특정 값 반환
    else:
        print(a[q[1]-1] + query(tempN, tree, 0, q[1]))
