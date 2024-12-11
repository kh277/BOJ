# 백준 13976

'''
분할 정복을 이용한 거듭제곱으로 O(N)인 DP 계산을 O(logN)으로 최적화해야 한다.
'''

import sys

input = sys.stdin.readline
MOD = 1000000007


def matrixMul(A, B):
    result = [[0, 0], [0, 0]]
    
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] = (result[i][j] + A[i][k]*B[k][j]) % MOD

    return result


def recur(A, powerCount):
    if powerCount == 1:
        return A
    elif powerCount == 2:
        return matrixMul(A, A)
    elif powerCount % 2 == 0:
        result = recur(A, powerCount//2)
        return matrixMul(result, result)
    else:
        result = recur(A, (powerCount-1)//2)
        return matrixMul(matrixMul(result, result), A)


def solve():
    if N % 2 != 0:
        return 0
    elif N == 2:
        return 3
    elif N == 4:
        return 11
    else:
        result = recur([[4, -1], [1, 0]], (N-4)//2)
        return (result[0][0]*11 + result[0][1]*3) % MOD


# main 함수 ----------
N = int(input())
print(solve())
