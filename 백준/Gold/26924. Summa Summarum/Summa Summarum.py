# 백준 26924

'''
길이가 N인 두 배열이 주어질 때,
각 배열에서 수를 하나씩 선택하여 바꾼 뒤 합이 최소가 될 때의 합을 구하는 문제이다.

두 배열 모두 오름차순 정렬을 한 뒤, 투 포인터로 탐색하면 된다.
'''

import sys

input = sys.stdin.readline
INF = 10e11

def calculateGap(sumA, sumB, indexA, indexB):
    return sumA - A[indexA] + B[indexB], sumB - B[indexB] + A[indexA]


def solve():
    # A, B 정렬
    A.sort()
    B.sort()
    sumA = sum(A)
    sumB = sum(B)
    indexA = 0
    indexB = 0
    
    # 투 포인터를 이용해 합이 최소가 되도록 인덱스를 변경시켜가며 비교
    result = INF
    while indexA < N and indexB < N:
        newA, newB = calculateGap(sumA, sumB, indexA, indexB)
        gap = newA - newB

        if gap > 0:
            indexA += 1
            result = min(result, gap)
        elif gap < 0:
            indexB += 1
            result = min(result, -gap)
        else:
            return 0
    
    return result


# main 함수 ----------
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(solve())