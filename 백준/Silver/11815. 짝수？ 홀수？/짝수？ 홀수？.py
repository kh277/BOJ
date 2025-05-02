# 백준 11815

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N):
    rootN = N**0.5
    if int(rootN)**2 == N:
        return 1
        
    return 0


def main():
    N = int(input())
    for _ in range(N):
        for i in list(map(int, input().split())):
            print(solve(i), end=" ")


main()
    