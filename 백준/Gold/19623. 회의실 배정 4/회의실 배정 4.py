# 백준 19623

'''
LIS 문제의 세그먼트 트리 풀이와 거의 유사하다.
'''

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
ARRAY_TYPE = 'I'


def square(N):
    result = 2
    while True:
        if result >= N:
            return result
        else:
            result <<= 1


# 시작 시간, 끝 시간 압축
def compress(N, task):
    data = []
    for i in range(N):
        data.append(task[i][0])
        data.append(task[i][1])
    data.sort()

    compV = {x: i for i, x in enumerate(data)}
    for i in range(N):
        task[i][0] = compV[task[i][0]]
        task[i][1] = compV[task[i][1]]


# index번째 값을 value로 변경
def update(N, tree, index, value):
    index += N
    if tree[index] > value:
        return
    tree[index] = value

    while index > 1:
        index >>= 1
        tree[index] = max(tree[index<<1], tree[index<<1 | 1])


# 구간 [left, right] 내의 최대값을 구하는 쿼리
def query(N, tree, left, right):
    result = 0
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


def solve(N, task):
    # 좌표 압축
    compress(N, task)
    task.sort(key= lambda x: (x[1], x[0]))

    # 세그먼트 트리로 이전 값 관리 및 갱신
    size = square(2*N)
    tree = array(ARRAY_TYPE, [0]) * (size*2)

    for i in range(N):
        curS, curE, curV = task[i]
        maxV = 0
        if curS > 0:
            maxV = query(size, tree, 0, curS-1)
        update(size, tree, curE, maxV+curV)

    return tree[1]


def main():
    N = int(input())
    task = []
    for _ in range(N):
        task.append(list(map(int, input().split())))
    print(solve(N, task))


main()
