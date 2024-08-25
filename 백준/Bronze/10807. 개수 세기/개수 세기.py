# 백준 10807

import sys

input = sys.stdin.readline


def solve(num: list, v: int) -> int:
    result = 0
    for i in num:
        if i == v:
            result += 1

    return result

def main():
    N = int(input())
    num = list(map(int, input().split()))
    v = int(input())
    print(solve(num, v))


main()