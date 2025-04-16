# 백준 13417

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, cha):
    cur = cha[0]
    index = 1
    while index < N:
        left = cur[0]
        if ord(cha[index]) <= ord(left):
            cur = cha[index] + cur
        else:
            cur = cur + cha[index]
        index += 1

    return cur


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        cha = list(input().decode().strip().split())
        print(solve(N, cha))


main()
