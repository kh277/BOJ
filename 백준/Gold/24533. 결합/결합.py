# 백준 3186

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, mat):
    energy = 0
    curA, curB = mat[0]

    for i in range(1, N):
        curC, curD = mat[i]
        energy += curA*curD + curB*curC
        curA += curC
        curB += curD

    return energy


def main():
    N = int(input())
    mat = []
    for _ in range(N):
        mat.append(list(map(int, input().split())))
    print(solve(N, mat))


main()
