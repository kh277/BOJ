# 백준 14646

import sys

input = sys.stdin.readline


def solve(N: int, menu: list) -> int:
    visited = [False for _ in range(N+1)]
    result = 0
    count = 0

    for i in menu:
        if visited[i] == True:
            count -= 1
        else:
            visited[i] = True
            count += 1
            result = max(result, count)

    return result


def main():
    N = int(input())
    menu = list(map(int, input().split()))

    print(solve(N, menu))


main()