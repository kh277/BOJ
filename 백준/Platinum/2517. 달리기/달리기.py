# 백준 2517

'''
모든 선수들이 가질 수 있는 실력의 범위를 리프 노드에 저장해야 한다.
그러나 값의 범위가 10억이고, 선수의 수가 최대 50만명이므로 값 압축이 필요하다.

값 압축 후, 입력된 순서대로 이전에 입력된 선수 중 현재 선수의 실력보다 큰 값을 가지는 선수의 수를 세야 한다.
그냥 처리하긴 힘드므로 실력 내림차순으로 세그먼트 트리에 추가하고,
추가할 때 [0, index) 범위에 존재하는 선수의 수를 세면 된다.
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


# 각 선수의 실력 범위 압축
def compress(N, speed):
    speed.sort()

    before = speed[0][0]
    compress = 0
    for i in range(N):
        if speed[i][0] == before:
            speed[i][0] = compress
        else:
            before = speed[i][0]
            compress += 1
            speed[i][0] = compress

    # 실력 내림차순으로 정렬
    return sorted(speed, key= lambda x: -x[0])


# tree[index] 값을 1만큼 추가
def update(N, tree, index):
    index += N
    tree[index] = 1
    
    while index > 1:
        index >>= 1
        tree[index] = tree[index<<1] + tree[index<<1 | 1]


# [left, right) 범위에 존재하는 선수의 수 반환
def query(N, tree, left, right):
    result = 0
    left += N
    right += N
    
    while left <= right:
        # left가 홀수라면
        if left & 1:
            result += tree[left]
            left += 1
        # right가 짝수라면
        if ~right & 1:
            result += tree[right]
            right -= 1
            
        left >>= 1
        right >>= 1
    
    return result


def solve(N, speed):
    # [실력, 입력 인덱스] -> [압축 실력값, 입력 인덱스]로 데이터 압축
    speed = compress(tempN, speed)

    tree = [0 for _ in range(2*N)]
    result = [0 for _ in range(tempN)]

    # 실력이 큰 선수부터 세그먼트 트리의 입력 인덱스 위치에 추가
    for i in range(tempN):
        _, index = speed[i]
        update(N, tree, index)

        # [0, index) 범위에 있는 선수의 수 저장
        result[index] = query(N, tree, 0, index)

    return result


# main 함수 ----------
tempN = int(input())
speed = []
for i in range(tempN):
    speed.append([int(input()), i])

for i in solve(square(tempN), speed):
    print(i)