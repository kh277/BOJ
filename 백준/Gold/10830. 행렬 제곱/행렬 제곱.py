# 백준 10830

import sys

input = sys.stdin.readline
MOD = 1000


def matrixMul(A, B):
    result = [[0 for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] = (result[i][j] + A[i][k]*B[k][j]) % MOD

    return result


def recur(A, powerCount):
    if powerCount == 1:
        # MOD가 1000이지만, 원소의 값이 1000일 수 있으므로
        for i in range(N):
            for j in range(N):
                A[i][j] = A[i][j] % MOD
        return A

    elif powerCount == 2:
        return matrixMul(A, A)

    elif powerCount % 2 == 0:
        result = recur(A, powerCount//2)
        return matrixMul(result, result)

    else:
        result = recur(A, (powerCount-1)//2)
        return matrixMul(matrixMul(result, result), A)


# main 함수 ----------
N, B = map(int, input().split())
M = []
for _ in range(N):
    M.append(list(map(int, input().split())))
for i in recur(M, B):
    print(*i)
