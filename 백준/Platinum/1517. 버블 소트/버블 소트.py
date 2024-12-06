# 백준 1517

'''
버블 정렬에서 swap의 횟수는 i>j, A[i]<A[j]의 개수와 같다.
즉 배열 A에서 역쌍의 개수를 세는 문제와 같다.

배열에 들어있는 값인 A[i]의 범위에 대해 segTree를 생성하면 메모리 초과가 발생하므로,
인덱스 값인 N의 범위에 대해 segTree를 생성하자.
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
    result = 0

    # segTree 기본 설정
    MAX = expo(N)
    tree = [0 for _ in range(MAX*2)]

    # [값, 원본 인덱스] 순서로 저장
    sortA = sorted([[A[i], i] for i in range(N)])

    # value 값이 작은 수부터 segTree에 저장하며 역쌍 개수 세기
    for _, index in sortA:
        update(MAX, tree, index, 1)
        result += query(MAX, tree, index+1, MAX-1)

    return result


# main 함수 ----------
N = int(input())
A = list(map(int, input().split()))

print(solve())