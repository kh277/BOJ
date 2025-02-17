# 백준 15678

'''
N개의 징검다리에서 최대 D칸까지 점프 가능할 때,
N번째 징검다리까지 밟았을 때 최대값은
max(이전에 점프 가능한 구간에서 점프해서 cur번째 징검다리를 밟는 경우, cur번째 징검다리에서 시작하는 경우)가 된다.
즉, DP[i] = (i번째 징검다리를 밟았을 때 얻을 수 있는 최대의 점수)로 두자.
또한, 세그먼트 트리를 이용해 구간에 대한 max값을 구하면 된다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**10


# index번째 인덱스를 value로 변경
def update(N, tree, index, value):
    index += N
    tree[index] = value
    
    while index > 1:
        index >>= 1
        tree[index] = max(tree[index<<1], tree[index<<1 | 1])


# 구간 [left, right]에서 최대값 반환
def query(N, tree, left, right):
    result = -INF
    left += N
    right += N

    while left <= right:
        if left & 1:
            result = max(result, tree[left])
            left += 1
        if ~right & 1:
            result = max(result, tree[right])
            right -= 1

        left >>= 1
        right >>= 1

    return result


def solve():
    # tempN = square(N)
    DPTree = [-INF for _ in range(2*N)]

    # DP 누적합 처리
    update(N, DPTree, 0, num[0])    # DP[0] 계산
    for cur in range(1, N):
        curMax = max(query(N, DPTree, max(0, cur-D), cur-1)+num[cur], num[cur])
        update(N, DPTree, cur, curMax)

    return query(N, DPTree, 0, N-1)


# main 함수 ----------
N, D = map(int, input().split())
num = list(map(int, input().split()))

print(solve())