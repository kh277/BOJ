# 백준 11650

import sys

input = sys.stdin.readline


def solve(arr: list) -> list:
    arr.sort(key= lambda x: (x[0], x[1]))
    return arr


def main():
    N = int(input())
    arr = [(0, 0) for _ in range(N)]
    for i in range(N):
        arr[i] = tuple(map(int, input().split()))

    for i in solve(arr):
        print(*i)


main()
