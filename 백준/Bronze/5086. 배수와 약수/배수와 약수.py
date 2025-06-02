# 백준 5086

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(A, B):
    if B % A == 0:
        return 'factor'
    elif A % B == 0:
        return 'multiple'

    return 'neither'


def main():
    while True:
        A = list(map(int, input().split()))
        if A[0] == 0:
            break
        print(solve(A[0], A[1]))


main()
