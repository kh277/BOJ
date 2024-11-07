# 백준 17131

'''
어떤 점 (a, b)에 대해 y > b이고, x != a인 (x, y)의 개수를 구하는 문제이다.
스위핑을 통해 y좌표가 가장 큰 점부터 가장 작은 점까지 내려오면서 탐색하면 된다.

모든 점에 대해 위의 쿼리를 처리하려면 O(NlogN)이내로 처리해야 하므로 세그먼트 트리를 사용하자.
'''

import sys

input = sys.stdin.readline
MAX = 200000*2+1        # x좌표는 -20만 ~ 20만이므로 인덱스는 0 ~ 40만 부분에 저장


# 세그먼트 트리 구성
def init(N, tree):
    for i in range(N-1, 0, -1):
        tree[i] = tree[i<<1] + tree[i<<1 | 1]


# index번째 인덱스의 값을 value만큼 추가
def update(N, tree, index, value):
    index += N
    tree[index] += value
    
    while index > 1:
        index >>= 1
        tree[index] = tree[index<<1] + tree[index<<1 | 1]


# left ~ right까지의 합 계산
def query(N, tree, left, right):
    result = 0
    left += N
    right += N

    if left > right:
        return result
    
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


def solve(N, point):
    # y좌표가 작아지도록, x좌표가 커지도록 정렬
    point.sort(key= lambda x: (-x[1], x[0]))

    # 세그먼트 트리 기본 설정
    tree = [0 for _ in range(MAX*2)]

    # y좌표가 큰 점부터 세그먼트 트리에 추가 및 쿼리 처리
    result = 0
    curY = point[0][1]
    temp = []
    for i in range(N):
        # 이전에 탐색했던 점의 y좌표와 같다면 -> x좌표를 temp에 저장하고 쿼리 실행
        if curY == point[i][1]:
            temp.append(point[i][0])
        # 이전에 탐색했던 점의 y좌표보다 크다면 -> 같은 y좌표의 점들 전부 트리에 추가
        else:
            for j in temp:
                update(MAX, tree, j+MAX//2, 1)
            curY = point[i][1]
            temp = [point[i][0]]        # temp 배열 초기화
        
        # 자기 자신의 x좌표를 제외한 좌상단 및 우상단 별의 개수를 누적하여 저장
        result += (query(MAX, tree, point[i][0]+MAX//2+1, MAX-1) * query(MAX, tree, 0, point[i][0]+MAX//2-1)) % 1000000007

    return (result) % 1000000007


# main 함수 ----------
N = int(input())
point = []
for _ in range(N):
    point.append(list(map(int, input().split())))
    
print(solve(N, point))
