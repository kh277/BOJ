# 백준 12728

'''
3 + sqrt(5)는 x^2 - 6x + 4 = 0의 근이므로 이를 이용해 DP 점화식을 세운 뒤,
행렬곱을 이용해 분할정복으로 처리하면 된다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
MOD = 1000


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


def solve(N):
    if N == 1:
        return '005'

    coef = [[6, -4], [1, 0]]
    f0 = 2
    f1 = 6

    # coef N번 제곱
    recurResult = recur(coef, N-1)

    # f(n) 구하기
    result = (recurResult[0][0]*f1 + recurResult[0][1]*f0) % MOD

    # 소숫점 제거
    result = int(result) - 1
    return '0'*(3-len(str(result))) + str(result)


def main():
    T = int(input())
    for i in range(1, T+1):
        N = int(input())
        print('Case #{}: {}'.format(i, solve(N)))


main()
