# 백준 10830

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
MOD = 1000


def matrixMul(size, A, B):
    result = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] = (result[i][j] + A[i][k]*B[k][j]) % MOD

    return result


def solve(A, exp, size):
    R = [[0] * size for _ in range(size)]
    base = [i[:] for i in A]
    for y in range(size):
        for x in range(size):
            if y == x:
                R[y][x] = 1

    while exp:
        if exp & 1:
            R = matrixMul(size, R, base)

        base = matrixMul(size, base, base)
        exp >>= 1

    return R


def main():
    N, B = map(int, input().split())
    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))
    for i in solve(A, B, N):
        print(*i)


main()
