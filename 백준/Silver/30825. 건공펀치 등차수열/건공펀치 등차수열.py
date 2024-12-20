# 백준 30825

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve():
    before = A[0]
    for i in range(1, N):
        if A[i] > before+K:
            before = A[i]
        else:
            before = before + K

    curValue = before
    result = 0
    for i in range(N-1, -1, -1):
        gap = curValue - A[i] 
        result += gap
        curValue -= K

    return result


# main 함수 ----------
N, K = map(int, input().split())
A = list(map(int, input().split()))

print(solve())