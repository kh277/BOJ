# 백준 13752


import sys

input = sys.stdin.readline


def solve(data: int) -> int:
    return '=' * data


def main():
    N = int(input())
    
    for i in range(N):
        data = int(input())
        print(solve(data))


main()