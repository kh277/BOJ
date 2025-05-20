# 백준 1699

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N):
    one = set()
    for i in range(1, int(N**0.5)+1):
        cur = i**2
        if cur == N:
            return 1
        one.add(cur)

    two = set()
    for i in list(one):
        for j in list(one):
            cur = i + j
            if cur == N:
                return 2
            if cur not in one:
                two.add(cur)

    for i in list(one):
        for j in list(two):
            cur = i + j
            if cur == N:
                return 3

    return 4


def main():
    N = int(input())
    print(solve(N))


main()
