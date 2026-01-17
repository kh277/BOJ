# 백준 34927

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, A):
    A.sort()
    index = 0
    accSum = 0
    count = 0

    while index < N:
        if A[index] >= accSum:
            accSum += A[index]
            count += 1
        index += 1
    
    return count


def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(solve(N, A))


main()
