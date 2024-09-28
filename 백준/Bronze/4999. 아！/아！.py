# 백준 4999


import sys

input = sys.stdin.readline


def solve(A: str, B: str) -> str:
    return 'no' if len(A) < len(B) else 'go'


def main():
    A = input().rstrip()
    B = input().rstrip()
    print(solve(A, B))


main()