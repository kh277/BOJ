# 백준 12515

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, A):
    count = 0
    for i in range(1, N+1):
        if A[i-1] != i:
            count += 1

    return count


def main():
    T = int(input())
    for i in range(1, T+1):
        N = int(input())
        A = list(map(int, input().split()))

        print(f"Case #{i}: {solve(N, A)}.000000")


main()
