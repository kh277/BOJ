# 백준 15810

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
MOD = 1000000007


def solve(N, A):
    total = sum(A)
    result = total*total - sum([A[i]*A[i] for i in range(N)])
    return result//2 % MOD


def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(solve(N, A))


main()
