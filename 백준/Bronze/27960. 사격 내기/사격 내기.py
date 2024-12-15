# 백준 27960

import sys

input = sys.stdin.readline


def solve(A, B):
    case = [512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
    numA = [False for _ in range(len(case))]
    numB = [False for _ in range(len(case))]
    for i in range(len(case)):
        if A - case[i] >= 0:
            numA[i] = True
            A -= case[i]
        if B - case[i] >= 0:
            numB[i] = True
            B -= case[i]
    
    result = 0
    for i in range(len(case)):
        if numA[i] != numB[i]:
            result += case[i]
    
    return result


# main 함수 ----------
A, B = map(int, input().split())
print(solve(A, B))