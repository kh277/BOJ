# 백준 15624

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
MOD = 1000000007


# 행렬 A와 B의 곱 반환
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


def main():
    N = int(input())
    if N == 0:
        print(0)
        return
    print(recur([[1, 1], [1, 0]], N)[0][1])


main()
