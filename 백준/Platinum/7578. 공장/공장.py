# 백준 1517

'''
segTree를 이용해서 역쌍 개수를 구하면 된다.
'''

import sys

input = sys.stdin.readline


def expo(N):
    result = 2
    while True:
        if result >= N:
            return result
        else:
            result *= 2


# index번째 값을 value만큼 추가
def update(N, tree, index, value):
    index += N
    tree[index] += value

    while index > 1:
        index >>= 1
        tree[index] = tree[index<<1] + tree[index<<1 | 1]


# left ~ right 까지의 합 구하기
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


def solve():
    # 기계의 식별번호 압축
    dic = dict()
    for i in range(N):
        dic[A[i]] = i
    for i in range(N):
        B[i] = dic[B[i]]

    result = 0

    # segTree 기본 설정
    MAX = expo(N)
    tree = [0 for _ in range(MAX*2)]

    # [값, 원본 인덱스] 순서로 저장
    sortA = sorted([[B[i], i] for i in range(N)])

    # value 값이 작은 수부터 segTree에 저장하며 역쌍 개수 세기
    for _, index in sortA:
        update(MAX, tree, index, 1)
        result += query(MAX, tree, index+1, MAX-1)

    return result


# main 함수 ----------
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(solve())