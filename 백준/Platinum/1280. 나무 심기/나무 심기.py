# 백준 1280

'''
나무의 위치로 가능한 좌표가 0 ~ 20만이므로 각 좌표를 세그먼트 트리의 리프 노드로 설정한다.
줄기 노드에는 [나무가 심겨진 자식 노드의 좌표의 개수, 나무가 심겨진 자식 노드의 좌표 총합]을 저장한다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
MOD = 1000000007
MAX = 262144        # 20만을 넘는 2의 제곱수 중 최소값


# x = index에 나무 1개 추가
def update(index):
    index += MAX
    tree[index][0] += 1
    tree[index][1] += index-MAX

    while index > 1:
        index >>= 1
        tree[index][0] = tree[index<<1][0] + tree[index<<1 | 1][0]
        tree[index][1] = tree[index<<1][1] + tree[index<<1 | 1][1]


# left ~ right까지 현재 심어진 나무 좌표의 총합 및 개수 반환
def query(left, right):
    result = [0, 0]     # [좌표 개수, 좌표 총합]
    left += MAX
    right += MAX

    while left <= right:
        if left & 1:
            result[0] += tree[left][0]
            result[1] += tree[left][1]
            left += 1
        if ~right & 1:
            result[0] += tree[right][0]
            result[1] += tree[right][1]
            right -= 1

        left >>= 1
        right >>= 1

    return result


# main 함수 ----------
N = int(input())
tree = [[0, 0] for _ in range(2*MAX)]

# 입력 및 쿼리 수행
pos = int(input())
update(pos)

result = 1
for _ in range(N-1):
    pos = int(input())
    countL, resultL = query(0, pos-1)
    countR, resultR = query(pos+1, MAX-1)

    result = (result * (pos*countL - resultL + resultR - pos*countR)%MOD) % MOD
    update(pos)

print(result)