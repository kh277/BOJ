# 백준 2804

import sys

input = sys.stdin.readline


def check(A, B):
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i] == B[j]:
                return [i, j]


def solve():
    meetA, meetB = check(A, B)

    result = [['.' for _ in range(len(A))] for _ in range(len(B))]
    
    for i in range(len(A)):
        result[meetB][i] = A[i]
        
    for j in range(len(B)):
        result[j][meetA] = B[j]

    return result


# main 함수 ----------
A, B = map(str, input().split())

for i in solve():
    print(''.join(i))
