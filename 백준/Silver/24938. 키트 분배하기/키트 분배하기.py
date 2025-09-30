# 백준 24938

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, A):
    need = sum(A)//N
    result = 0
    left = 0
    for i in range(N):
        gap = need - A[i]
        
        left += gap
        result += abs(left)

    return result


def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(solve(N, A))


main()
